# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Reserva(models.Model):
    _name = 'reserva'
    _description = 'Reserva'
    _rec_name = 'persona'
    _order = 'fecha_reserva desc'

    persona = fields.Char(string='Persona', required=True)
    # Texto para conservar ceros iniciales, prefijo internacional y espacios
    telefono = fields.Char(string='Teléfono')
    fecha_reserva = fields.Date(string='Fecha de reserva')
    fecha_devolucion = fields.Date(string='Fecha de devolución')
    duracion = fields.Integer(string='Duración (días)', compute='_compute_duracion', store=True)
    libro_id = fields.Many2one('libro', string='Libro', required=True)

    @api.depends('fecha_reserva', 'fecha_devolucion')
    def _compute_duracion(self):
        for record in self:
            if record.fecha_reserva and record.fecha_devolucion:
                delta = record.fecha_devolucion - record.fecha_reserva
                record.duracion = delta.days
            else:
                record.duracion = 0

    @api.constrains('fecha_reserva', 'fecha_devolucion')
    def _check_fechas(self):
        for record in self:
            if (record.fecha_reserva and record.fecha_devolucion
                    and record.fecha_devolucion < record.fecha_reserva):
                raise ValidationError(
                    'La fecha de devolución no puede ser anterior a la fecha de reserva.')

    @api.constrains('libro_id', 'fecha_reserva', 'fecha_devolucion')
    def _check_solapamiento(self):
        for record in self:
            if not (record.libro_id and record.fecha_reserva):
                continue
            # Sin fecha de devolución, la reserva se considera abierta hasta que se devuelva
            dominio = [
                ('id', '!=', record.id),
                ('libro_id', '=', record.libro_id.id),
                '|', ('fecha_devolucion', '=', False),
                     ('fecha_devolucion', '>=', record.fecha_reserva),
            ]
            if record.fecha_devolucion:
                dominio += ['|', ('fecha_reserva', '=', False),
                                 ('fecha_reserva', '<=', record.fecha_devolucion)]
            otra = self.search(dominio, limit=1)
            if otra:
                raise ValidationError(
                    'El libro "%s" ya está reservado por %s en esas fechas.'
                    % (record.libro_id.nombre, otra.persona))
