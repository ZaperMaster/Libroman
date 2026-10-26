# -*- coding: utf-8 -*-
{
    'name': 'reserva',
    'version': '1.1',
    'category': 'Biblioteca',
    'summary': 'Reservas y préstamos de libros',
    'description': '''
        Reservas de los libros del catálogo con cálculo automático de los días de préstamo.
        Impide fechas de devolución anteriores a la reserva y reservas solapadas del mismo libro.
    ''',
    'author': 'ZaperMaster',
    'website': 'https://github.com/ZaperMaster/Libroman',
    'depends': ['base', 'libro'],
    'data': [
        'security/ir.model.access.csv',
        'views/reserva_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
