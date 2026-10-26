# -*- coding: utf-8 -*-
"""Renombra las columnas antiguas (Nombre, Autor...) a minúsculas sin perder datos."""

COLUMNAS = {
    'Nombre': 'nombre',
    'Autor': 'autor',
    'ISBN': 'isbn',
    'FechaSalida': 'fecha_salida',
    'Genero': 'genero',
}


def migrate(cr, version):
    if not version:
        return
    for antigua, nueva in COLUMNAS.items():
        cr.execute(
            "SELECT 1 FROM information_schema.columns "
            "WHERE table_name = 'libro' AND column_name = %s", (antigua,))
        if cr.fetchone():
            cr.execute('ALTER TABLE libro RENAME COLUMN "%s" TO "%s"' % (antigua, nueva))
