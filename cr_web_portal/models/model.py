# -*- coding: utf-8 -*-

from odoo.osv import expression
import babel.dates
from odoo import api, models, _
from odoo.tools import (
    clean_context, config, CountingStream, date_utils, discardattr,
    DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, frozendict,
    get_lang, LastOrderedSet, lazy_classproperty, OrderedSet, ormcache,
    partition, populate, Query, ReversedIterable, split_every, unique,
)
import datetime
from markupsafe import escape
from odoo.tools import pycompat
from markupsafe import Markup
from collections import OrderedDict
import dateutil
import pytz
class BaseModelExtend(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def _read_group_format_result(self, data, annotated_groupbys, groupby, domain):
        sections = []
        for gb in annotated_groupbys:
            ftype = gb['type']
            value = data[gb['groupby']]

            # full domain for this groupby spec
            d = None
            if value:
                if ftype in ['many2one', 'many2many']:
                    value = value[0]
                elif ftype in ('date', 'datetime'):
                    locale = get_lang(self.env).code
                    fmt = DEFAULT_SERVER_DATETIME_FORMAT if ftype == 'datetime' else DEFAULT_SERVER_DATE_FORMAT
                    tzinfo = None
                    range_start = value
                    range_end = value + gb['interval']
                    # if gb['granularity'] == 'year':
                    #     range_start = datetime(range_start.year, 4, 1)
                    #     range_end = datetime(range_end.year, 3, 31)
                    # value from postgres is in local tz (so range is
                    # considered in local tz e.g. "day" is [00:00, 00:00[
                    # local rather than UTC which could be [11:00, 11:00]
                    # local) but domain and raw value should be in UTC
                    if gb['tz_convert']:
                        tzinfo = range_start.tzinfo
                        range_start = range_start.astimezone(pytz.utc)
                        # take into account possible hour change between start and end
                        if tzinfo:
                            range_end = tzinfo.localize(range_end.replace(tzinfo=None))
                            range_end = range_end.astimezone(pytz.utc)

                    range_start = range_start.strftime(fmt)
                    range_end = range_end.strftime(fmt)
                    if ftype == 'datetime':
                        label = babel.dates.format_datetime(
                            value, format=gb['display_format'],
                            tzinfo=tzinfo, locale='en_IN'
                        )

                        if gb['display_format'] == 'yyyy':
                            label = '%s-%s' % (value.year, str(value.year + 1)[2:])

                        elif gb['display_format'] == 'QQQ yyyy':
                            if value.month == 4:
                                label = '%s %s-%s' % ('Q1', value.year, str(value.year + 1)[2:])
                            elif value.month == 7:
                                label = '%s %s-%s' % ('Q2', value.year, str(value.year + 1)[2:])
                            elif value.month == 10:
                                label = '%s %s-%s' % ('Q3', value.year, str(value.year + 1)[2:])
                            elif value.month == 1:
                                label = '%s %s-%s' % ('Q4', value.year - 1, str(value.year)[2:])
                    else:
                        label = babel.dates.format_date(
                            value, format=gb['display_format'],
                            locale=locale
                        )

                        if gb['display_format'] == 'yyyy':
                            label = '%s-%s' % (value.year, str(value.year + 1)[2:])

                        elif gb['display_format'] == 'QQQ yyyy':
                            if value.month == 4:
                                label = '%s %s-%s' % ('Q1', value.year, str(value.year + 1)[2:])
                            elif value.month == 7:
                                label = '%s %s-%s' % ('Q2', value.year, str(value.year + 1)[2:])
                            elif value.month == 10:
                                label = '%s %s-%s' % ('Q3', value.year, str(value.year + 1)[2:])
                            elif value.month == 1:
                                label = '%s %s-%s' % ('Q4', value.year - 1, str(value.year)[2:])

                    data[gb['groupby']] = ('%s/%s' % (range_start, range_end), label)
                    data.setdefault('__range', {})[gb['groupby']] = {'from': range_start, 'to': range_end}
                    d = [
                        '&',
                        (gb['field'], '>=', range_start),
                        (gb['field'], '<', range_end),
                    ]
            elif ftype in ('date', 'datetime'):
                # Set the __range of the group containing records with an unset
                # date/datetime field value to False.
                data.setdefault('__range', {})[gb['groupby']] = False

            if d is None:
                d = [(gb['field'], '=', value)]
            sections.append(d)
        sections.append(domain)

        data['__domain'] = expression.AND(sections)
        if len(groupby) - len(annotated_groupbys) >= 1:
            data['__context'] = {'group_by': groupby[len(annotated_groupbys):]}
        del data['id']
        return data

    @api.model
    def _read_group_process_groupby(self, gb, query):
        """
            Helper method to collect important information about groupbys: raw
            field name, type, time information, qualified name, ...
        """
        split = gb.split(':')
        field = self._fields.get(split[0])
        if not field:
            raise ValueError("Invalid field %r on model %r" % (split[0], self._name))
        field_type = field.type
        gb_function = split[1] if len(split) == 2 else None
        temporal = field_type in ('date', 'datetime')
        tz_convert = field_type == 'datetime' and self._context.get('tz') in pytz.all_timezones
        qualified_field = self._inherits_join_calc(self._table, split[0], query)
        if temporal:
            display_formats = {
                # Careful with week/year formats:
                #  - yyyy (lower) must always be used, *except* for week+year formats
                #  - YYYY (upper) must always be used for week+year format
                #         e.g. 2006-01-01 is W52 2005 in some locales (de_DE),
                #                         and W1 2006 for others
                #
                # Mixing both formats, e.g. 'MMM YYYY' would yield wrong results,
                # such as 2006-01-01 being formatted as "January 2005" in some locales.
                # Cfr: http://babel.pocoo.org/en/latest/dates.html#date-fields
                'hour': 'hh:00 dd MMM',
                'day': 'dd MMM yyyy',  # yyyy = normal year
                'week': "'W'w YYYY",  # w YYYY = ISO week-year
                'month': 'MMMM yyyy',
                'quarter': 'QQQ yyyy',
                'year': 'yyyy',
            }
            time_intervals = {
                'hour': dateutil.relativedelta.relativedelta(hours=1),
                'day': dateutil.relativedelta.relativedelta(days=1),
                'week': datetime.timedelta(days=7),
                'month': dateutil.relativedelta.relativedelta(months=1),
                'quarter': dateutil.relativedelta.relativedelta(months=3),
                'year': dateutil.relativedelta.relativedelta(years=1)
            }
            if tz_convert:
                qualified_field = "timezone('%s', timezone('UTC',%s))" % (
                self._context.get('tz', 'UTC'), qualified_field)
            if gb_function == 'year':
                qualified_field = """
                        CASE
                            WHEN EXTRACT(MONTH FROM %(qualified_field)s) >= 4
                            THEN date_trunc('year', %(qualified_field)s) + interval '3 months'
                            ELSE date_trunc('year', %(qualified_field)s) - interval '9 months'
                        END
                        """ % {'qualified_field': qualified_field}
            else:
                qualified_field = "date_trunc('%s', %s::timestamp)" % (gb_function or 'month', qualified_field)
        if field_type == 'boolean':
            qualified_field = "coalesce(%s,false)" % qualified_field
        return {
            'field': split[0],
            'groupby': gb,
            'type': field_type,
            'display_format': display_formats[gb_function or 'month'] if temporal else None,
            'interval': time_intervals[gb_function or 'month'] if temporal else None,
            'granularity': gb_function or 'month' if temporal else None,
            'tz_convert': tz_convert,
            'qualified_field': qualified_field,
        }

class Image(models.AbstractModel):
    _inherit = 'ir.qweb.field.image'

    @api.model
    def record_to_html(self, record, field_name, options):
        assert options['tagName'] != 'img',\
            "Oddly enough, the root tag of an image field can not be img. " \
            "That is because the image goes into the tag, or it gets the " \
            "hose again."
        src = src_zoom = None
        if 'zoom' in options and not options.get('zoom') and options.get('type') and options.get('type') == 'image':
            options['zoom'] = 'image_1920'
        if options.get('qweb_img_raw_data', False):
            value = record[field_name]
            if value is False:
                return False
            src = self._get_src_data_b64(value, options)
        else:
            src, src_zoom = self._get_src_urls(record, field_name, options)

        aclasses = ['img', 'img-fluid'] if options.get('qweb_img_responsive', True) else ['img']
        aclasses += options.get('class', '').split()
        classes = ' '.join(map(escape, aclasses))

        if options.get('alt-field') and options['alt-field'] in record and record[options['alt-field']]:
            alt = escape(record[options['alt-field']])
        elif options.get('alt'):
            alt = options['alt']
        else:
            alt = escape(record.display_name)

        itemprop = None
        if options.get('itemprop'):
            itemprop = options['itemprop']

        atts = OrderedDict()
        atts["src"] = src
        atts["itemprop"] = itemprop
        atts["class"] = classes
        atts["style"] = options.get('style')
        atts["width"] = options.get('width')
        atts["height"] = options.get('height')
        atts["alt"] = alt
        atts["data-zoom"] = src_zoom and u'1' or None
        atts["data-zoom-image"] = src_zoom
        atts["data-no-post-process"] = options.get('data-no-post-process')

        atts = self.env['ir.qweb']._post_processing_att('img', atts)

        img = ['<img']
        for name, value in atts.items():
            if value:
                img.append(' ')
                img.append(escape(pycompat.to_text(name)))
                img.append('="')
                img.append(escape(pycompat.to_text(value)))
                img.append('"')
        img.append('/>')

        return Markup(''.join(img))