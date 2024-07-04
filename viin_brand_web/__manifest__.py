{
    'name': "Web Debranding for Viindoo",
    'name_vi_VN': "",

    'summary': """
Debranding Web Builder for Viindoo""",

    'summary_vi_VN': """
Làm lại màu sắc Bộ công cụ dựng web theo thương hiệu Viindoo
        """,

    'description': """

Editions Supported
==================
1. Community Edition

    """,

    'description_vi_VN': """

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v16demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v16demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/Viindoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [],
    'assets': {
        'web.assets_backend': [
            'viin_brand_web/static/src/core/dialog/dialog.js',
        ],
    },
    'images': [
        # 'static/description/main_screenshot.png'
        ],
    'installable': True,
    'auto_install': True,
    'price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
