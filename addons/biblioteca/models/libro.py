from odoo import models, fields


class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro de la biblioteca'

    name = fields.Char(string='Titulo', required=True)
    autor = fields.Char(string='Autor')
    anio_publicacion = fields.Integer(string='Anio de publicacion')
    paginas = fields.Integer(string='Cantidad de paginas')
    disponible = fields.Boolean(string='Disponible', default=True)
    resumen = fields.Text(string='Resumen')
    # NIVEL 3: solo los administradores ven este campo
    precio_costo = fields.Float(string='Precio de costo', groups='base.group_system')
