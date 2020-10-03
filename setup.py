# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='''ckanext-archiveview''',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version='0.0.1',

    description='''A ckan extension that provides a resource view for zipped archives.''',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # The project's main homepage.
    url='https://github.com/fwoerister/ckanext-archiveview',

    # Author details
    author='''Florian Woerister''',
    author_email='''florian.woerister@tuwien.ac.at''',

    # Choose your license
    license='AGPLv3+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='''CKAN archive zip''',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    namespace_packages=['ckanext'],

    install_requires=[

    ],

    entry_points='''
        [ckan.plugins]
        archiveview=ckanext.archiveview.plugin:ArchiveViewPlugin
        
        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    ''',

    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    }
)
