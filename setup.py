#!/usr/bin/env python

from distutils.core import setup

setup(
        name='dbcps',
        version='0.1.1',
        long_description=open('README.md').read(),
        packages = [
                'dbcps',
                'dbcps.filters',
                'dbcps.sinks',
        ],
)
