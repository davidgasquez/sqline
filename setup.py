#!/usr/bin/env python

from setuptools import setup

requirements = [
    'click',
    'pandas',
    'sqlalchemy',
    'psycopg2'
]

setup(
    name='sqline',
    version='0.1.1',
    description="Command line tool to perform database queries.",
    author="David Gasquez",
    author_email='davidgasquez@gmail.com',
    url='https://github.com/davidgasquez/sqline',
    entry_points={
        'console_scripts': [
            'sqline=sqline:main'
        ]
    },
    py_modules=['sqline'],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='sqline'
)
