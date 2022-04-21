# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class PosOrderLine(models.Model):
    _name = 'kitchen.pos.order'
    _description = 'Kitchen POS Order'
    _rec_name = 'pos_id'

    pos_id = fields.Many2one('pos.order', string='Kitchen Order', required=True, readonly=True)
    lines = fields.Many2many('kitchen.pos.order.line', string='Lines', readonly=True)
    kitchen = fields.Html(string='Kitchen', compute='compute_kitchen', sanitize=False, readonly=True)

    def product_class_attr(self, line):
        product_class_attr = \
            ' class="kitchen-td-product" ' \
            f'kitchen-line-id="{line.id}"'
        return product_class_attr

    def product_info(self, line):
        product_info = \
            '<div>' \
            f'{line.product_id.name}' \
            '</div>' \
            '<div>' \
            f'{int(line.product_quantity)}x' \
            '</div>'
        return product_info

    def kitchen_products(self):
        lines = self.lines
        appetizer_hot = lines.filtered(
            lambda
                l: l.food_type == 'kitchen' and l.food_temperature == 'hot' and l.food_serve_as.name == 'Appetizer' and l.product_state == 'in progress')
        main_hot = lines.filtered(
            lambda
                l: l.food_type == 'kitchen' and l.food_temperature == 'hot' and l.food_serve_as.name == 'Main Dish' and l.product_state == 'in progress')
        dessert_hot = lines.filtered(
            lambda
                l: l.food_type == 'kitchen' and l.food_temperature == 'hot' and l.food_serve_as.name == 'Dessert' and l.product_state == 'in progress')
        appetizer_cold = lines.filtered(
            lambda
                l: l.food_type == 'kitchen' and l.food_temperature == 'cold' and l.food_serve_as.name == 'Appetizer' and l.product_state == 'in progress')
        main_cold = lines.filtered(
            lambda
                l: l.food_type == 'kitchen' and l.food_temperature == 'cold' and l.food_serve_as.name == 'Main Dish' and l.product_state == 'in progress')
        dessert_cold = lines.filtered(
            lambda
                l: l.food_type == 'kitchen' and l.food_temperature == 'cold' and l.food_serve_as.name == 'Dessert' and l.product_state == 'in progress')
        kitchen_depth = max([len(appetizer_hot), len(main_hot), len(dessert_hot), len(appetizer_cold), len(main_cold),
                             len(dessert_cold)])
        kitchen_products = ''
        for i in range(0, kitchen_depth):
            kitchen_products += \
                '<tr>' \
                f'<td{self.product_class_attr(line=appetizer_hot[i]) if i < len(appetizer_hot) else ""}>{self.product_info(line=appetizer_hot[i]) if i < len(appetizer_hot) else ""}</td>' \
                f'<td{self.product_class_attr(line=main_hot[i]) if i < len(main_hot) else ""}>{self.product_info(line=main_hot[i]) if i < len(main_hot) else ""}</td>' \
                f'<td{self.product_class_attr(line=dessert_hot[i]) if i < len(dessert_hot) else ""}>{self.product_info(line=dessert_hot[i]) if i < len(dessert_hot) else ""}</td>' \
                f'<td{self.product_class_attr(line=appetizer_cold[i]) if i < len(appetizer_cold) else ""}>{self.product_info(line=appetizer_cold[i]) if i < len(appetizer_cold) else ""}</td>' \
                f'<td{self.product_class_attr(line=main_cold[i]) if i < len(main_cold) else ""}>{self.product_info(line=main_cold[i]) if i < len(main_cold) else ""}</td>' \
                f'<td{self.product_class_attr(line=dessert_cold[i]) if i < len(dessert_cold) else ""}>{self.product_info(line=dessert_cold[i]) if i < len(dessert_cold) else ""}</td>' \
                '</tr>'
        return kitchen_products

    def bar_products(self):
        lines = self.lines
        appetizer_hot = lines.filtered(
            lambda
                l: l.food_type == 'bar' and l.food_temperature == 'hot' and l.food_serve_as.name == 'Appetizer' and l.product_state == 'in progress')
        main_hot = lines.filtered(
            lambda
                l: l.food_type == 'bar' and l.food_temperature == 'hot' and l.food_serve_as.name == 'Main Dish' and l.product_state == 'in progress')
        dessert_hot = lines.filtered(
            lambda
                l: l.food_type == 'bar' and l.food_temperature == 'hot' and l.food_serve_as.name == 'Dessert' and l.product_state == 'in progress')
        appetizer_cold = lines.filtered(
            lambda
                l: l.food_type == 'bar' and l.food_temperature == 'cold' and l.food_serve_as.name == 'Appetizer' and l.product_state == 'in progress')
        main_cold = lines.filtered(
            lambda
                l: l.food_type == 'bar' and l.food_temperature == 'cold' and l.food_serve_as.name == 'Main Dish' and l.product_state == 'in progress')
        dessert_cold = lines.filtered(
            lambda
                l: l.food_type == 'bar' and l.food_temperature == 'cold' and l.food_serve_as.name == 'Dessert' and l.product_state == 'in progress')
        bar_depth = max([len(appetizer_hot), len(main_hot), len(dessert_hot), len(appetizer_cold), len(main_cold),
                         len(dessert_cold)])
        bar_products = ''
        for i in range(0, bar_depth):
            bar_products += \
                '<tr>' \
                f'<td{self.product_class_attr(line=appetizer_hot[i]) if i < len(appetizer_hot) else ""}>{self.product_info(line=appetizer_hot[i]) if i < len(appetizer_hot) else ""}</td>' \
                f'<td{self.product_class_attr(line=main_hot[i]) if i < len(main_hot) else ""}>{self.product_info(line=main_hot[i]) if i < len(main_hot) else ""}</td>' \
                f'<td{self.product_class_attr(line=dessert_hot[i]) if i < len(dessert_hot) else ""}>{self.product_info(line=dessert_hot[i]) if i < len(dessert_hot) else ""}</td>' \
                f'<td{self.product_class_attr(line=appetizer_cold[i]) if i < len(appetizer_cold) else ""}>{self.product_info(line=appetizer_cold[i]) if i < len(appetizer_cold) else ""}</td>' \
                f'<td{self.product_class_attr(line=main_cold[i]) if i < len(main_cold) else ""}>{self.product_info(line=main_cold[i]) if i < len(main_cold) else ""}</td>' \
                f'<td{self.product_class_attr(line=dessert_cold[i]) if i < len(dessert_cold) else ""}>{self.product_info(line=dessert_cold[i]) if i < len(dessert_cold) else ""}</td>' \
                '</tr>'
        return bar_products

    def kitchen_title(self):
        kitchen_title = \
            '<div class="row">' \
            '<div class="col-lg-12 col-12">' \
            '<div>' \
            f'<h1 class="font-weight-bold font-italic">{self.pos_id.name}</h2>' \
            '</div>' \
            '<div class="mt32">' \
            '<button class="btn btn-primary btn-lg text-white btn-show-kitchen" style="width: 125px;">' \
            '<i class="fa fa-cutlery pr-2"/>' \
            '<span>' \
            + _('Kitchen') + \
            '</span>' \
            '</button>' \
            '&nbsp;&nbsp;&nbsp;' \
            '<button class="btn btn-primary btn-lg text-white btn-show-bar" style="width: 125px;">' \
            '<i class="fa fa-glass pr-2"/>' \
            '<span>' \
            + _('Bar') + \
            '</span>' \
            '</button>' \
            '</div>' \
            '</div>' \
            '</div>'
        return kitchen_title

    def kitchen_screen(self):
        kitchen_products = self.kitchen_products()
        kitchen_screen = \
            '<div class="kitchen-screen mt32">' \
            '<div class="text-center">' \
            f'<h1 class="font-weight-bold font-italic">' \
            + _('Kitchen Screen') + \
            f'</h1>' \
            '</div>' \
            '<table class="table table-responsive table-bordered table-hover kitchen-table w-100 d-block d-md-table">' \
            '<thead>' \
            '<tr>' \
            '<th class="hot-kitchen-bg">' \
            + _('Appetizer') + \
            '</th>' \
            '<th class="hot-kitchen-bg">' \
            + _('Main') + \
            '</th>' \
            '<th class="hot-kitchen-bg">' \
            + _('Dessert') + \
            '</th>' \
            '<th class="cold-kitchen-bg">' \
            + _('Appetizer') + \
            '</th>' \
            '<th class="cold-kitchen-bg">' \
            + _('Main') + \
            '</th>' \
            '<th class="cold-kitchen-bg">' \
            + _('Dessert') + \
            '</th>' \
            '</tr>' \
            '</thead>' \
            '<tbody>' \
            f'{kitchen_products}' \
            '</tbody>' \
            '</table>' \
            '</div>'
        return kitchen_screen

    def bar_screen(self):
        bar_products = self.bar_products()
        bar_screen = \
            '<div class="bar-screen mt32 d-none">' \
            '<div class="text-center">' \
            f'<h1 class="font-weight-bold font-italic">' \
            + _('Bar Screen') + \
            f'</h1>' \
            '</div>' \
            '<table class="table table-responsive table-bordered table-hover kitchen-table w-100 d-block d-md-table">' \
            '<thead>' \
            '<tr>' \
            '<th class="hot-kitchen-bg">' \
            + _('Appetizer') + \
            '</th>' \
            '<th class="hot-kitchen-bg">' \
            + _('Main') + \
            '</th>' \
            '<th class="hot-kitchen-bg">' \
            + _('Dessert') + \
            '</th>' \
            '<th class="cold-kitchen-bg">' \
            + _('Appetizer') + \
            '</th>' \
            '<th class="cold-kitchen-bg">' \
            + _('Main') + \
            '</th>' \
            '<th class="cold-kitchen-bg">' \
            + _('Dessert') + \
            '</th>' \
            '</tr>' \
            '</thead>' \
            '<tbody>' \
            f'{bar_products}' \
            '</tbody>' \
            '</table>' \
            '</div>'
        return bar_screen

    def ready_products(self):
        lines = self.lines
        lines = lines.filtered(lambda l: l.product_state == 'ready')
        ready_products = ''
        for line in lines:
            ready_products += \
                '<div class="kitchen-item">' \
                '<div>' \
                f'<span>{line.product_id.name}</span>' \
                f'<br/>' \
                f'<span>{int(line.product_quantity)}x</span>' \
                '</div>' \
                '</div>'
        ready_products = \
            '<div class="row mt32">' \
            '<div class="ready-products col-lg-12 d-flex" style="overflow-x: auto; white-space: nowrap;">' \
            '<div class="kitchen-item kitchen-ready-item">' \
            '<div>' \
            '<span>' \
            + _('Ready') + \
            '</span>' \
            '</div>' \
            '</div>' \
            f'{ready_products}' \
            '</div>' \
            '</div>'
        return ready_products

    def togo_products(self):
        lines = self.lines
        lines = lines.filtered(lambda l: l.product_state == 'to go')
        togo_products = ''
        for line in lines:
            togo_products += \
                '<div class="kitchen-item">' \
                '<div>' \
                f'<span>{line.product_id.name}</span>' \
                f'<br/>' \
                f'<span>{int(line.product_quantity)}x</span>' \
                '</div>' \
                '</div>'
        togo_products = \
            '<div class="row mt32">' \
            '<div class="col-lg-12 d-flex" style="overflow-x: auto; white-space: nowrap;">' \
            '<div class="kitchen-item kitchen-togo-item">' \
            '<div>' \
            '<span>' \
            + _('To Go') + \
            '</span>' \
            '</div>' \
            '</div>' \
            f'{togo_products}' \
            '</div>' \
            '</div>'
        return togo_products

    def compute_kitchen(self):
        for record in self:
            kitchen_title = self.kitchen_title()
            kitchen_screen = self.kitchen_screen()
            bar_screen = self.bar_screen()
            ready_products = self.ready_products()
            togo_products = self.togo_products()
            record.kitchen = f'{kitchen_title}' \
                             f'<div class="row">' \
                             '<div class="col-lg-12 col-12">' \
                             f'{kitchen_screen}' \
                             f'{bar_screen}' \
                             '</div>' \
                             '</div>' \
                             f'{ready_products}' \
                             f'{togo_products}'

    @api.model
    def product_to_ready(self, line):
        line = self.env['kitchen.pos.order.line'].search([('id', '=', int(line))])
        line.write({'product_state': 'ready'})
        content = \
            '<div class="kitchen-item">' \
            '<div>' \
            f'<span>{line.product_id.name}</span>' \
            f'<br/>' \
            f'<span>{int(line.product_quantity)}x</span>' \
            '</div>' \
            '</div>'
        return content
