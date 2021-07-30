from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.move.line'
    # _inherit = ['stock.move', 'stock.move.line']

    # product_id = fields.Many2one("product.template")
    # pcs_per_cartoon = fields.Integer(related="product_id.pcs_per_cartoon", string="Number of cartons")
    pcs_per_cartoon = fields.Integer(string="Number of cartons")

