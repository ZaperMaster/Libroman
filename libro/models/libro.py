# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Libro(models.Model):
    _name = 'libro'
    _description = 'Libro'

    Nombre = fields.Char(string='Nombre')
    Autor = fields.Char(string='Autor')
    ISBN = fields.Char(string='ISBN')
    FechaSalida = fields.Datetime(string='FechaSalida')
    Genero = fields.Char(string='Genero')
