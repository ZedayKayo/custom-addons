# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Duplicated Contacts',
    'version': '1.3',
    'category': 'Hidden',
    'description': """
Duplicated Contacts To Add Fields To Contact view.
===================================================
""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        #'views/dup_contact.xml',
        'views/contact.xml',
    ],
    'sequence':'-100',
    'demo': [
    ],
    'test': [],
    'installable': True,
    'auto_install': True,
    'application': True,
    'license': 'LGPL-3',
}
