# -*- coding: utf-8 -*-
{
    'name': 'ARA Simplify Access Management',
    'version': '19.0.0.0.0',
    'category': 'Extra Tools',
    'summary': 'All-in-one access control for fields, models, menus, records, & system UI, plus complete white-label debranding.',
    'description': """
Simplify Access Management & System Debranding
==============================================
Centralize user permission controls and system branding settings in one place. Restrict actions and UI elements by User, Group, or Company.

Core Features:
--------------
* Model & Field Controls: Set Read-Only, Hidden, or Required properties. Prohibit Create, Edit, Delete, Import, and Export per model.
* Record & Menu Visibility: Granular access using custom domain filters; hide top menus and submenus effortlessly.
* Interface Customization: Hide specific views, action buttons, tabs, filters, reports, and Chatter options (logs, messages, activities).
* System Security Enforcement: Restrict Developer Mode, module installation/upgrades, data export, and external XML-RPC requests.
* White-Labeling (Debranding): Remove Odoo logos, branding tags, and external references across the platform.
""",
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
            'ara_simplify_access_management/static/src/**/*',
        ],
    },
    "images": ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'price': 99.00,
    'currency': "USD",

}