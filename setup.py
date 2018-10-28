#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from distutils.core import setup

version = '0.0.1'

setup(name='aioiotprov',
    packages=['aioiotprov'],
    version=version,
    author='François Wautier',
    author_email='francois@wautier.eu',
    description='Library/utility to help provision various IoT devices. ',
    url='http://github.com/frawau/aioiotprov',
    download_url='https://github.com/frawau/aioiotprov/archive/'+version+'.tar.gz',
    keywords = ['IoT', 'provisioning', 'automation'],
    license='MIT',
    install_requires=[
    "aiohttp"
    ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ])