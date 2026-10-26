# -*- coding: utf-8 -*-
"""Renombra las columnas antiguas (Persona, Telefono...) a minúsculas sin perder datos.

El teléfono pasa de número entero a texto: la columna se convierte aquí para que Odoo
no la descarte al ver el cambio de tipo.
"""

COLUMNAS = {
    'Persona': 'persona',
    'Telefono': 'telefono',
    'FechaReserva': 'fecha_reserva',
    'FechaDevolucion': 'fecha_devolucion',
    'Duracion': 'duracion',
    'Libro': 'libro_id',
}


def migrate(cr, version):
    if not version:
        return
    for antigua, nueva in COLUMNAS.items():
        cr.execute(
            "SELECT 1 FROM information_schema.columns "
            "WHERE table_name = 'reserva' AND column_name = %s", (antigua,))
        if cr.fetchone():
            cr.execute('ALTER TABLE reserva RENAME COLUMN "%s" TO "%s"' % (antigua, nueva))
    cr.execute(
        "SELECT data_type FROM information_schema.columns "
        "WHERE table_name = 'reserva' AND column_name = 'telefono'")
    fila = cr.fetchone()
    if fila and fila[0] != 'character varying':
        cr.execute('ALTER TABLE reserva ALTER COLUMN telefono TYPE varchar USING telefono::varchar')
