# 📚 Libroman

Gestión de una pequeña biblioteca en **Odoo**: catálogo de libros y control de reservas y
préstamos, repartido en dos módulos independientes.

**Compatible con Odoo 18.**

| Módulo | Qué hace | Depende de |
|---|---|---|
| [`libro`](libro/) | Catálogo de libros: título, autor, ISBN, fecha de publicación y género | `base` |
| [`reserva`](reserva/) | Reservas de libros: quién, cuándo y por cuántos días | `base`, `libro` |

## Funcionalidades

### Módulo `libro`
- Alta, edición, consulta y borrado de libros.
- Vista de lista con todos los campos y formulario dividido en dos bloques.
- Menú propio **Libro** en la barra de aplicaciones de Odoo.
- Define los grupos de permisos de la biblioteca (ver [Permisos](#permisos)).

| Campo | Tipo | Descripción |
|---|---|---|
| `nombre` | Texto (obligatorio) | Título del libro; es el nombre que se muestra al elegirlo en una reserva |
| `autor` | Texto | Autor o autora |
| `isbn` | Texto | Código ISBN |
| `fecha_salida` | Fecha y hora | Fecha de publicación |
| `genero` | Texto | Género literario |

### Módulo `reserva`
- Registro de reservas enlazadas a un libro del catálogo.
- **Cálculo automático de la duración**: al indicar la fecha de reserva y la de devolución,
  Odoo calcula los días del préstamo y los guarda (`store=True`), así que se puede ordenar
  y filtrar por ellos.
- **Validaciones**: la fecha de devolución no puede ser anterior a la de reserva, y un
  mismo libro no puede tener dos reservas con fechas que se solapen (una reserva sin
  fecha de devolución se considera abierta).
- Menú propio **Reserva** en la barra de aplicaciones.

| Campo | Tipo | Descripción |
|---|---|---|
| `persona` | Texto (obligatorio) | Quién reserva el libro |
| `telefono` | Texto | Teléfono de contacto (admite prefijo `+`, ceros iniciales y espacios) |
| `libro_id` | Relación (`Many2one` → `libro`, obligatorio) | Libro reservado |
| `fecha_reserva` | Fecha | Inicio del préstamo |
| `fecha_devolucion` | Fecha | Fin del préstamo |
| `duracion` | Número (calculado, solo lectura) | Días entre reserva y devolución |

## Permisos

El módulo `libro` crea la categoría **Biblioteca** con dos grupos, que se asignan en
*Ajustes → Usuarios*:

| Grupo | Libros | Reservas |
|---|---|---|
| **Usuario** | Consultar | Consultar, crear y editar |
| **Bibliotecario** | Todo (incluido borrar) | Todo (incluido borrar) |

Los menús solo se ven con alguno de estos grupos. El administrador recibe
**Bibliotecario** al instalar el módulo.

## Estructura

```
libro/
├── __manifest__.py              Datos del módulo y dependencias
├── models/libro.py              Modelo `libro`
├── migrations/1.1/              Renombra las columnas de la versión 1.0
├── security/
│   ├── libro_security.xml       Grupos Usuario y Bibliotecario
│   └── ir.model.access.csv      Permisos de cada grupo
├── static/description/icon.png  Icono de la aplicación
└── views/
    ├── libro_views.xml          Vistas de lista y formulario + acción
    └── menu_views.xml           Menús
reserva/
├── __manifest__.py
├── models/reserva.py            Modelo `reserva`, duración y validaciones
├── migrations/1.1/              Renombra columnas y convierte el teléfono a texto
├── security/ir.model.access.csv
├── static/description/icon.png
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

> Las vistas de lista usan la etiqueta `<list>` de **Odoo 18**. Para Odoo 17 o anterior
> hay que volver a `<tree>` y cambiar `view_mode` de `list,form` a `tree,form`, o usar la
> [versión 1.1](https://github.com/ZaperMaster/Libroman/tree/f556c9e).

## Uso

1. Abre **Libro** y da de alta los libros de la biblioteca.
2. Abre **Reserva**, crea una reserva, elige el libro y rellena las fechas.
3. El campo **Duración** se rellena solo con los días de préstamo.

## Actualizar desde la versión 1.0

La versión 1.1 (incluida en la 1.2) cambia los nombres de los campos a minúsculas (`Nombre` → `nombre`,
`Libro` → `libro_id`…) y el teléfono de número a texto. Los scripts de `migrations/1.1/`
renombran las columnas antes de cargar el módulo, así que **no se pierden datos**: basta
con actualizar `libro` y `reserva` desde *Aplicaciones* (o con `-u libro,reserva`).

## Cambios de la versión 1.1

- Icono propio para cada módulo (`static/description/icon.png`).
- Teléfono guardado como texto: conserva ceros iniciales, prefijo `+` y espacios.
- La fecha de devolución no puede ser anterior a la de reserva.
- Un mismo libro no puede tener dos reservas que se solapen.
- Permisos por grupos: **Usuario** y **Bibliotecario**.
- Nombres de campo en minúsculas, como recomienda la guía de estilo de Odoo.
- Los libros se muestran por su título al elegirlos en una reserva (antes salía `libro,1`).

## Cambios de la versión 1.2

- Compatibilidad con Odoo 18: vistas `<list>` y `view_mode` `list,form`.

## Autor

Hecho por [ZaperMaster](https://github.com/ZaperMaster).
