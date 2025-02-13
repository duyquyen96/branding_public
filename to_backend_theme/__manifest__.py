# Copyright 2016, 2019 Openworx - Mario Gielissen
# Copyright 2012, 2019 Openworx - T.V.T Marine Automation
# Copyright 2019,2021 Viindoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Viindoo Backend Theme",
    "summary": "Mobile backend theme for Odoo community",

	"description": """
Backend theme for Viindoo, based on the Openworx Backend Theme

    """,

    'author': 'Openworx,T.V.T Marine Automation,Viindoo',
    'website': 'https://viindoo.com',
    'live_test_url': "https://v16demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v16demo-vn.viindoo.com",
    'support': 'apps.support@viindoo.com',

    # Categories can be used to filter modules in modules listing
    'category': 'Website/Theme/Backend',
    'version': '1.0.24',

    "depends": [
        'web',
        'web_editor',
        'web_responsive',
        'viin_brand_common',
    ],
    "data": [
        'views/web.xml'
    ],
    'images': [
        'images/screen.png'
    ],
    'assets': {
        'web.assets_backend': [
            ('after', 'web/static/src/views/form/form_controller.scss', 'to_backend_theme/static/src/views/form/form_controller.scss'),
            ('after', '/web_responsive/static/src/legacy/scss/web_responsive.scss', '/to_backend_theme/static/src/legacy/scss/web_responsive.scss'),
            ('after', '/web_responsive/static/src/components/apps_menu/apps_menu.scss', 'to_backend_theme/static/src/scss/apps_menu.scss'),
            'to_backend_theme/static/src/scss/style.scss',
            ('after', 'web/static/src/views/pivot/pivot_view.scss', 'to_backend_theme/static/src/views/pivot/pivot_view.scss'),
            ('after', 'web/static/src/legacy/scss/kanban_dashboard.scss', 'to_backend_theme/static/src/views/kanban/kanban_dashboard.scss'),
            ],
        },
    'installable': True,
    'application': False,
    'auto_install': ['web'],
    'price': 99.9,
    'currency': 'EUR',
    'license': 'LGPL-3',
}
