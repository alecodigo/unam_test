# -*- coding: utf-8 -*-

{
    'name': 'Sistema de Gestión de Inscripciones',
    'version': '0.1',
    'author': 'Alejandro Sánchez',
    'sequence': 1,
    'summary': 'Sistema de Gestión de Inscripciones',
    'description': """
        Sistema de gestion de inscripciones de un sistema educativo.
    """,
    'depends': [
        'base',
        'contacts',
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/inscription_views.xml',
        'views/professor_views.xml',
        'views/student_views.xml',
        'views/subject_views.xml',
        'views/unam_test_menus.xml',
    ],
    'demo': [
        # 'data/course_demo.xml',
        # 'data/professor_demo.xml',
        # 'data/student_demo.xml',
        # 'data/subject_demo.xml',
        'data/unam_test_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3', 

}