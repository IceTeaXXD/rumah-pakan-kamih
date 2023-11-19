{
    'name': "Rumah Pakan Kamih",
    'summary': 'Module Odoo untuk Sistem Informasi terpusat Rumah Pakan Kamih.',
    'description': 'Module Odoo untuk sistem pengelolaan barang gudang dan sistem manajemen reservasi.',
    'sequence': -100,
    'author': "Angger Business Firm",
    'category': 'Uncategorized',
    'version': '16.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/rpk_menus.xml',
        'views/rpk_forms.xml',
        'views/rpk_trees.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
