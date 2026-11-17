{
    'name': 'Biblioteca',
    'version': '1.0',
    'summary': 'Modulo del curso: modelos, vistas, seguridad y web publica',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/biblioteca_libro_views.xml',
        'views/biblioteca_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'biblioteca/static/src/scss/biblioteca.scss',
        ],
    },
    'installable': True,
    'application': True,
}
