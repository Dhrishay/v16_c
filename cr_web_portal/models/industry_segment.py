# -*- coding: utf-8 -*-

import logging
from datetime import datetime, timedelta
from collections import defaultdict

from odoo import models, fields


class IndustrySegment(models.Model):
    _name = 'industry.segment'

    name = fields.Text('Name')
    main_category = fields.Many2one('main.category',string='Main Category')
    sub_category = fields.Many2many('sub.category','industry_segment_sub_category','industry_segment','sub_category',string='Sub Category')

class MainCategory(models.Model):
    _name = 'main.category'

    name = fields.Text('Name')

class SubCategory(models.Model):
    _name = 'sub.category'

    name = fields.Text('Name')
    industry_segment = fields.Many2many('industry.segment','industry_segment_sub_category','sub_category','industry_segment',string='Industry Segment')
