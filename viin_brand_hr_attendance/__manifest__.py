{
    'name': "Viindoo Branding Attendances",
    'name_vi_VN': "Ứng dụng Attendances với thương hiệu Viindoo",

    'summary': """
Set Viindoo Brandings for Attendances app.
""",

    'summary_vi_VN': """
Thiết lập thương hiệu Viindoo cho ứng dụng Attendances
    	""",

    'description': """
This module change some information for Viindoo branding
 
Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,

    'description_vi_VN': """
Mô đun này thay đổi một vài thông tin dành riêng cho thương hiệu Viindoo

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "T.V.T Marine Automation (aka TVTMA)",
    'website': "https://www.tvtmarine.com",
    'live_test_url': "https://v13demo-int.erponline.vn",
    'support': "support@ma.tvtmarine.com",
    'category': 'Human Resources/Attendances',
    'version': '0.1',
    'depends': ['hr_attendance', 'viin_brand_base'],
    'images' : [
    	'static/description/icon.png'
	],
    'data' : [
        'data/update_icon.xml'
    ],
    'installable': True,
    'uninstall_hook': '_uninstall_brand_icon',
    'application': False,
    'auto_install': True,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
