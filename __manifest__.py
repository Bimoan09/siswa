# -*- coding: utf-8 -*-
{
    'name': "Siswa",

    'summary': """
        Modul siswa""",

    'description': """
        Modul Siswa
    """,

    'author': "Bimo Anugrah Prasetyo",
    'website': "http://www.yourcompany.com",


    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/Siswa.xml',
        'views/Guru.xml',
        'views/Kelas.xml',
        'views/Mata_Pelajaran.xml',
        'views/templates.xml',
        'report/siswa_report.xml',
        'report/siswa_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
