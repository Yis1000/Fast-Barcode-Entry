{
    'name': 'Fast Barcode Entry',
    'version': '19.0.1.0.0',
    'summary': 'Añade y actualiza códigos de barras directamente desde la recepción de mercancía',
    'description': """
Entrada de Código de Barras en Recepción
========================================

Optimiza tu proceso de entrada de recepcion gestionando los códigos de barras directamente desde las operaciones de stock.

Características Principales
---------------------------
* **Entrada Directa**: Añade una columna de **'Código de Barras'** en las líneas de operaciones del albarán de recepción.
* **Guardado Automático**: Cualquier código escaneado o escrito en este campo se **guarda automáticamente** en la ficha del producto asociado.
* **Mayor Eficiencia**: Evita tener que navegar a la ficha del producto para asignar un código de barras nuevo durante la entrada de stock.

Cómo Funciona
-------------
1. Navega a **Inventario > Operaciones > Transferencias** (o Recepciones).
2. Abre un albarán de entrada.
3. En la pestaña **Operaciones**, encontrarás la nueva columna **Código de Barras**.
4. Escanea con tu lector o escribe el código manualmente. El sistema lo asignará al producto al instante.
    """,
    'category': 'Inventory/Inventory',
    'author': 'Yis1000',
    'maintainer': 'Yis1000',
    'website': 'https://github.com/Yis1000',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
