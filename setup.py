"""
Uses setuptools to make our local mkdocs-scoped-nav plugin available to MkDocs.
"""
from setuptools import setup

setup(
    name='mkdocs-scoped-nav',
    version='0.1',
    packages=['plugins'],
    entry_points={
        'mkdocs.plugins': [
            'scoped-nav = plugins.scoped_nav:ScopedNavPlugin'
        ]
    }
)
