from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_custom_notes = fields.Text(string='Custom Notes')
