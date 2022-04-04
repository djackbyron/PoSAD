# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class KitchenController(http.Controller):

    @http.route(['/get_kitchen_view'], type='json', auth="user", website=False)
    def get_kitchen_view(self):
        action = request.env.ref('kitchen_pos.kitchen_action')
        model = 'kitchen.pos.order'
        menu = request.env.ref('kitchen_pos.kitchen_menu')
        return f'/web#action={action.id}&model={model}&menu_id={menu.id}'
