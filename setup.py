from setuptools import setup

setup(
    name='pemweb',
    install_requires=[
        'pyramid',
        'waitress',
        'sqlalchemy',
        'zope.sqlalchemy',
        'pyramid_tm',
        'pyramid_jinja2',
    ],
    entry_points={
        'paste.app_factory': [
            'main = pemweb:main',
        ],
    },
)
