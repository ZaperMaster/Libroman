# -*- coding: utf-8 -*-

from odoo import models, fields


class Libro(models.Model):
    _name = 'libro'
    _description = 'Libro'
    _rec_name = 'nombre'
    _order = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    autor = fields.Char(string='Autor')
    isbn = fields.Char(string='ISBN')
    fecha_salida = fields.Datetime(string='Fecha de salida')
    genero = fields.Char(string='Género')
