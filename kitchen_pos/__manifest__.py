# -*- coding: utf-8 -*-
{
    'name': 'Kitchen POS',
    'version': '14.0.1.0.0',
    'summary': 'Kitchen POS',
    'description': 'Kitchen POS',
    'category': 'Website',
    'author': 'Bojan Anchev',
    'depends': ['base', 'web', 'point_of_sale'],
    'data': [
        # security
        'security/ir.model.access.csv',
        # data
        'data/doneness.xml',
        'data/serve_as.xml',
        # views
        'views/assets.xml',
        'views/kitchen_pos.xml',
        'views/product.xml',
        'views/pos_order.xml'
    ],
    'qweb': [
        'static/src/xml/kitchen.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
