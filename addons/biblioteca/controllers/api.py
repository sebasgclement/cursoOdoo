from odoo import http
from odoo.http import request


class BibliotecaAPI(http.Controller):

    # API: devuelve los libros en JSON, para que OTRO programa los consuma
    @http.route('/api/libros', type='json', auth='public', methods=['POST'])
    def api_libros(self, **kwargs):
        libros = request.env['biblioteca.libro'].sudo().search(
            [('disponible', '=', True)]
        )
        return [
            {
                'titulo': libro.name,
                'autor': libro.autor,
                'anio': libro.anio_publicacion,
            }
            for libro in libros
        ]
