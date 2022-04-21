# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class KitchenPosLine(models.Model):
    _name = "kitchen.pos.order.line"
    _description = "Kitchen POS Order Line"

    pos_order_line = fields.Many2one('pos.order.line', string='POS Order Line', required=True, readonly=True)
    product_id = fields.Many2one('product.product', string='Product', related='pos_order_line.product_id',
                                 readonly=True)
    product_quantity = fields.Float(string='Product Quantity', related='pos_order_line.qty', readonly=True)
    product_state = fields.Selection([('in progress', 'In Progress'), ('to go', 'To Go'), ('ready', 'Ready')],
                                     string='Product State', readonly=True, default='in progress')
    food_type = fields.Selection([('kitchen', 'Kitchen'), ('bar', 'Bar')], string='Type',
                                 related='pos_order_line.product_id.food_type', readonly=True)
    food_temperature = fields.Selection([('hot', 'Hot'), ('cold', 'Cold')], string='Temperature',
                                        related='pos_order_line.product_id.food_temperature', readonly=True)
    food_serve_as = fields.Many2one('product.serve.as', string='Serve As', related='pos_order_line.food_serve_as',
                                    readonly=True)
