from odoo import _, api, fields, models


class PartnerMailListWizard(models.TransientModel):
    _name = "partner.mail.list.wizard"
    _description = "Create contact mailing list"

    mail_list_id = fields.Many2one(comodel_name="mailing.list", string="Mailing List")
    partner_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="mail_list_wizard_partner",
        default=lambda self: self.env.context.get("active_ids"))

    def add_to_mail_list(self):
        contact_obj = self.env["mailing.contact"]
        partners = self.partner_ids
        for partner in partners:
            if partner.email:
                mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                if mailing_contact_id and self.mail_list_id.id not in mailing_contact_id.list_ids.ids:
                    mailing_contact_id.list_ids = [(4, self.mail_list_id.id)]
                elif not mailing_contact_id:
                    contact_vals = {
                        "name": partner.name,
                        "email": partner.email,
                        "list_ids": [(4, self.mail_list_id.id)],
                        "company_name": partner.company_id.name or False,
                        "country_id": partner.country_id.id or False,
                        "opt_out": True if not partner.opt_out else False
                    }
                    mailing_contact_id = contact_obj.create(contact_vals)
                self.env.cr.commit()
                if mailing_contact_id:
                    subscription_line_id = mailing_contact_id.subscription_list_ids.filtered(lambda x: x.list_id and x.list_id.id == self.mail_list_id.id)
                    if subscription_line_id:
                        subscription_line_id.opt_out = True if not partner.opt_out else False


class CRMMailListWizard(models.TransientModel):
    _name = "crm.mail.list.wizard"
    _description = "Create contact mailing list"

    mail_list_id = fields.Many2one(comodel_name="mailing.list", string="Mailing List")
    lead_ids = fields.Many2many(
        comodel_name="crm.lead",
        relation="mail_list_wizard_crm",
        default=lambda self: self.env.context.get("active_ids"))

    def add_to_mail_list(self):
        contact_obj = self.env["mailing.contact"]
        lead_ids = self.lead_ids
        for lead in lead_ids:
            if lead.partner_id:
                partner = lead.partner_id
                if partner.email:
                    mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                    if mailing_contact_id and self.mail_list_id.id not in mailing_contact_id.list_ids.ids:
                        mailing_contact_id.list_ids = [(4, self.mail_list_id.id)]
                    elif not mailing_contact_id:
                        contact_vals = {
                            "name": partner.name,
                            "email": partner.email,
                            "list_ids": [(4, self.mail_list_id.id)],
                            "company_name": partner.company_id.name or False,
                            "country_id": partner.country_id.id or False,
                            "opt_out": True if not partner.opt_out else False
                        }
                        contact_obj.create(contact_vals)
            elif lead.email_from:
                mailing_contact_id = contact_obj.search([('email', '=', lead.email_from)], limit=1)
                if mailing_contact_id and self.mail_list_id.id not in mailing_contact_id.list_ids.ids:
                    mailing_contact_id.list_ids = [(4, self.mail_list_id.id)]
                elif not mailing_contact_id:
                    name = ''
                    if lead.contact_name:
                        name = lead.contact_name
                    elif lead.partner_name:
                        name = lead.partner_name
                    contact_vals = {
                        "name": name,
                        "email": lead.email_from,
                        "list_ids": [(4, self.mail_list_id.id)],
                        "country_id": lead.country_id.id or False,
                    }
                    contact_obj.create(contact_vals)

class SaleOrderMailListWizard(models.TransientModel):
    _name = "sale.order.mail.list.wizard"
    _description = "Create contact mailing list"

    mail_list_id = fields.Many2one(comodel_name="mailing.list", string="Mailing List")
    order_ids = fields.Many2many(
        comodel_name="sale.order",
        relation="mail_list_wizard_sale_order",
        default=lambda self: self.env.context.get("active_ids"))

    def add_to_mail_list(self):
        contact_obj = self.env["mailing.contact"]
        order_ids = self.order_ids
        for order in order_ids:
            if order.partner_id:
                partner = order.partner_id
                if partner.email:
                    mailing_contact_id = contact_obj.search([('email', '=', partner.email)], limit=1)
                    if mailing_contact_id and self.mail_list_id.id not in mailing_contact_id.list_ids.ids:
                        mailing_contact_id.list_ids = [(4, self.mail_list_id.id)]
                    elif not mailing_contact_id:
                        contact_vals = {
                            "name": partner.name,
                            "email": partner.email,
                            "list_ids": [(4, self.mail_list_id.id)],
                            "company_name": partner.company_id.name or False,
                            "country_id": partner.country_id.id or False,
                            "opt_out": True if not partner.opt_out else False
                        }
                        contact_obj.create(contact_vals)