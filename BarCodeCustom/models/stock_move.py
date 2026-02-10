from odoo import models, fields

# heredo del modelo stock.move que son las lineas del albaran
class StockMove(models.Model):
    _inherit = 'stock.move'

    # campo relacionado con el barcode del producto
    # le pongo readonly false para poder escribir en el y que se guarde
    product_barcode_scan = fields.Char(
        related='product_id.barcode',
        readonly=False,
        string='codigo de barras',
        help="escribe aqui el codigo de barras para guardarlo en el producto"
    )
