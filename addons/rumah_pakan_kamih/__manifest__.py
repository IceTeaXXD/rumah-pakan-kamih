# -*- coding: utf-8 -*-
{
    'name': "Rumah Pakan Kamih",
    'summary': 'Module Odoo untuk Sistem Informasi terpusat Rumah Pakan Kamih.',
    'description': 'Module Odoo untuk sistem pengelolaan barang gudang dan sistem manajemen reservasi.',
    'author': "Angger Business Firm",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['hotel','hotel_reservation'],
    'data': [
        'security/ir.model.access.csv',
        'views/rpk_menus.xml',
        'views/rpk_trees.xml',
        'views/rpk_forms.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'auto_install': False,
}
