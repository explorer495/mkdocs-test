"""
Uses setuptools to make our local mkdocs-scoped-nav plugin available to MkDocs.
"""
from setuptools import setup

setup(
    name='dccex-mkdocs-plugins',
    version='0.0.2',
    packages=['plugins'],
    entry_points={
        'mkdocs.plugins': [
            'scoped-nav = plugins.scoped_nav:ScopedNavPlugin',
            'latest-news = plugins.latest_news:LatestNewsPlugin'
        ]
    }
)
