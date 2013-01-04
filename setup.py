# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]

setup( 
        name='timeout-decorator',
        version='0.1.0',
        description='Timeout decorator',
        long_description = open('README.rst').read(),
        author='PN',
        author_email='pn.appdev@gmail.com',
        url='https://github.com/pnpnpn/timeout-decorator',
        packages=['timeout_decorator'],
        install_requires=[],
        classifiers=CLASSIFIERS)


