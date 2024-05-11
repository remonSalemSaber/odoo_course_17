# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Real State',
    'version' : '17.0.0.0.1',
    'summary': 'Manage Real State',
    'author': 'Remon Salem',
    'sequence': -1,
    'description': """Module to manage real state cycle""",
    'category': 'Sales',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/real_state_view.xml'
    ],

    'installable': True,
    'application': True,

    'license': 'LGPL-3',
}