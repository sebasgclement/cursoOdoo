from odoo import http
from odoo.http import request


class BibliotecaWeb(http.Controller):

    # Pagina publica: cualquiera puede entrar a /biblioteca sin login
    @http.route('/biblioteca', type='http', auth='public', website=False)
    def lista_libros(self, **kwargs):
        libros = request.env['biblioteca.libro'].sudo().search(
            [('disponible', '=', True)]
        )
        return request.render('biblioteca.pagina_libros', {
            'libros': libros,
        })
