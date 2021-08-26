from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.move.line'
    pcs_per_cartoon = fields.Integer(string="Number of cartons")


