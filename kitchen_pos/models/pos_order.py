# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class PosOrder(models.Model):
    _inherit = 'pos.order'

    kitchen_pos_order_id = fields.Many2one('kitchen.pos.order', required=False, string='Kitchen Order', readonly=True)

    @api.model
    def create(self, vals):
        pos_order = super(PosOrder, self).create(vals)
        kitchen_pos_order = self.env['kitchen.pos.order'].create({'pos_id': pos_order.id})
        pos_order.write({'kitchen_pos_order_id': kitchen_pos_order.id})
        kitchen_pos_order_line_ids = []
        for line in pos_order.lines:
            kitchen_line = self.env['kitchen.pos.order.line'].create({'pos_order_line': line.id})
            kitchen_pos_order_line_ids.append(kitchen_line.id)
        kitchen_pos_order.write({'lines': [(6, 0, kitchen_pos_order_line_ids)]})
        return pos_order

    def unlink(self):
        for record in self:
            if record.kitchen_pos_order_id:
                record.kitchen_pos_order_id.unlink()
        return super(PosOrder, self).unlink()

    def kitchen_pos_order_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'kitchen.pos.order',
            'view_mode': 'form',
            'views': [[False, 'form']],
            'res_id': self.kitchen_pos_order_id.id
        }

    @api.constrains('lines')
    def kitchen_pos_order_check(self):
        if self.kitchen_pos_order_id:
            raise ValidationError(
                _('This operation is not allowed because the Point of Sale order is tied to a Kitchen Order.'))
