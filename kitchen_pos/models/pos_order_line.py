from odoo import fields, models, api, _


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    food_type = fields.Selection([('kitchen', 'Kitchen'), ('bar', 'Bar')], string='Type', related='product_id.food_type', required=False)
    food_temperature = fields.Selection([('hot', 'Hot'), ('cold', 'Cold')], string='Temperature', related='product_id.food_temperature', required=False)
    food_serve_as = fields.Many2one('product.serve.as', string='Serve As', required=False)
    food_doneness = fields.Many2one('product.food.doneness', string='Doneness', required=False)
    note = fields.Text(string='Note')
