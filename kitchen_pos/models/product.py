# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ProductServeAs(models.Model):
    _name = 'product.serve.as'
    _description = 'Product Serve As'

    name = fields.Char(string='Name', required=True)


class ProductDoneness(models.Model):
    _name = 'product.food.doneness'
    _description = 'Product Doneness'

    name = fields.Char(string='Name', required=True)


class PosOrderLine(models.Model):
    _inherit = 'product.product'

    food_type = fields.Selection([('kitchen', 'Kitchen'), ('bar', 'Bar')], string='Type', required=True)
    food_temperature = fields.Selection([('hot', 'Hot'), ('cold', 'Cold')], string='Temperature', required=True)
    food_serve_as = fields.Many2many('product.serve.as', string='Serve As', required=True)
    food_doneness = fields.Many2many('product.food.doneness', string='Doneness', required=False)
