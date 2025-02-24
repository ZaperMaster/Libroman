# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class Reserva(models.Model):
    _name = 'reserva'
    _description = 'Reserva'

    Persona = fields.Char(string='Persona')
    Telefono = fields.Integer(string='Telefono')
    FechaReserva = fields.Date(string='FechaReserva')
    FechaDevolucion = fields.Date(string='FechaDevolucion')
    Duracion = fields.Integer(string='Duracion', compute='_compute_duracion', store=True)
    Libro = fields.Many2one('libro', string='Libro')

    @api.depends('FechaReserva', 'FechaDevolucion')
    def _compute_duracion(self):
        for record in self:
            if record.FechaReserva and record.FechaDevolucion:
                delta = record.FechaDevolucion - record.FechaReserva
                record.Duracion = delta.days
            else:
                record.Duracion = 0
