# 📚 Libroman

Gestión de una pequeña biblioteca en **Odoo**: catálogo de libros y control de reservas y
préstamos, repartido en dos módulos independientes.

| Módulo | Qué hace | Depende de |
|---|---|---|
| [`libro`](libro/) | Catálogo de libros: título, autor, ISBN, fecha de publicación y género | `base` |
| [`reserva`](reserva/) | Reservas de libros: quién, cuándo y por cuántos días | `base`, `libro` |

## Funcionalidades

### Módulo `libro`
- Alta, edición, consulta y borrado de libros.
- Vista de lista con todos los campos y formulario dividido en dos bloques.
- Menú propio **Libro** en la barra de aplicaciones de Odoo.

| Campo | Tipo | Descripción |
|---|---|---|
| `Nombre` | Texto | Título del libro |
| `Autor` | Texto | Autor o autora |
| `ISBN` | Texto | Código ISBN |
| `FechaSalida` | Fecha y hora | Fecha de publicación |
| `Genero` | Texto | Género literario |

### Módulo `reserva`
- Registro de reservas enlazadas a un libro del catálogo.
- **Cálculo automático de la duración**: al indicar la fecha de reserva y la de devolución,
  Odoo calcula los días del préstamo y los guarda (`store=True`), así que se puede ordenar
  y filtrar por ellos.
- Menú propio **Reserva** en la barra de aplicaciones.

| Campo | Tipo | Descripción |
|---|---|---|
| `Persona` | Texto | Quién reserva el libro |
| `Telefono` | Número | Teléfono de contacto |
| `Libro` | Relación (`Many2one` → `libro`) | Libro reservado |
| `FechaReserva` | Fecha | Inicio del préstamo |
| `FechaDevolucion` | Fecha | Fin del préstamo |
| `Duracion` | Número (calculado, solo lectura) | Días entre reserva y devolución |

## Estructura

```
libro/
├── __manifest__.py              Datos del módulo y dependencias
├── models/libro.py              Modelo `libro`
├── security/ir.model.access.csv Permisos de acceso
└── views/
    ├── libro_views.xml          Vistas de lista y formulario + acción
    └── menu_views.xml           Menús
reserva/
├── __manifest__.py
├── models/reserva.py            Modelo `reserva` y cálculo de la duración
├── security/ir.model.access.csv
└── views/
    ├── reserva_views.xml
    └── menu_views.xml
```

## Instalación

1. Copia las carpetas `libro` y `reserva` en una ruta incluida en el `addons_path` de tu
   instancia de Odoo, por ejemplo:

   ```bash
   git clone https://github.com/ZaperMaster/Libroman.git
   cp -r Libroman/libro Libroman/reserva /ruta/a/odoo/custom-addons/
   ```

2. Reinicia el servidor de Odoo.
3. Activa el **modo desarrollador** (*Ajustes → Activar el modo de desarrollador*).
4. En **Aplicaciones**, pulsa *Actualizar lista de aplicaciones*.
5. Busca e instala **libro** y después **reserva** (si instalas primero `reserva`, Odoo
   instalará `libro` automáticamente por la dependencia).

> Las vistas de lista usan la etiqueta `<tree>`, válida hasta **Odoo 17**. En Odoo 18 hay
> que cambiarla por `<list>` y `view_mode` de `tree,form` a `list,form`.

## Uso

1. Abre **Libro** y da de alta los libros de la biblioteca.
2. Abre **Reserva**, crea una reserva, elige el libro y rellena las fechas.
3. El campo **Duración** se rellena solo con los días de préstamo.

## Mejoras pendientes

- [ ] Añadir el icono `static/description/icon.png` que usan los menús.
- [ ] Guardar el teléfono como texto (con un número entero se pierden los ceros iniciales y el prefijo `+`).
- [ ] Validar que la fecha de devolución no sea anterior a la de reserva.
- [ ] Impedir que un mismo libro tenga dos reservas que se solapen.
- [ ] Restringir los permisos por grupos (ahora cualquier usuario puede leer, crear, editar y borrar).
- [ ] Nombres de campo en minúsculas (`nombre`, `autor`…), como recomienda la guía de estilo de Odoo.

## Autor

Hecho por [ZaperMaster](https://github.com/ZaperMaster).
