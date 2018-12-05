"""Setuptools entry point."""
import codecs
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

dirname = os.path.dirname(__file__)

long_description = (
    codecs.open(os.path.join(dirname, 'README.rst'), encoding='utf-8').read() + '\n' +
    codecs.open(os.path.join(dirname, 'CHANGES.rst'), encoding='utf-8').read()
)

setup(
    name='timeout-decorator',
    version='0.4.1',
    description='Timeout decorator',
    long_description=long_description,
    author='Patrick Ng',
    author_email='pn.appdev@gmail.com',
    url='https://github.com/pnpnpn/timeout-decorator',
    packages=['timeout_decorator'],
    install_requires=[],
    classifiers=CLASSIFIERS)
