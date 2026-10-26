# -*- coding: utf-8 -*-
{
    'name': 'libro',
    'version': '1.1',
    'category': 'Biblioteca',
    'summary': 'Catálogo de libros de la biblioteca',
    'description': '''
        Catálogo de libros: título, autor, ISBN, fecha de publicación y género.
        Define los grupos de la biblioteca (Usuario y Bibliotecario) que usa el módulo reserva.
    ''',
    'author': 'ZaperMaster',
    'website': 'https://github.com/ZaperMaster/Libroman',
    'depends': ['base'],
    'data': [
        'security/libro_security.xml',
        'security/ir.model.access.csv',
        'views/libro_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
