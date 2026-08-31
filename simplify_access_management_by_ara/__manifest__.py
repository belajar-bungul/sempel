# -*- coding: utf-8 -*-
{
    'name': 'Simplify Access Management ODOO By ARA',
    'version': '19.0.0.0.0',
    'category': 'Extra Tools',
    'summary': 'All-in-one access control for fields, models, menus, records, & system UI, plus complete white-label debranding.',
    'author': 'ARA SOFT',
    'maintainer': 'ARA SOFT',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['web', 'mail', 'base_import', 'bus', 'rpc'],
    'data': [
        'security/sam_security.xml',
        'security/ir.model.access.csv',
        'views/sam_profile_views.xml',
        'debranding/views/debranding_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'simplify_access_management_by_ara/static/src/**/*',
        ],
    },
    "images": ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'price': 99.00,
    'currency': "USD",

}