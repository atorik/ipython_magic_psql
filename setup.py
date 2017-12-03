# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ipython_magic_psql',
    version='0.1.0',
    description='psql wrapper magic command',
    long_description=readme,
    author='atorik',
    author_email='atorik@gmail.com',
    url='https://github.com/atorik/magic_psql',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'pexpect',
        'ipython',
    ],
)

