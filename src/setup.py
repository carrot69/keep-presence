#!/usr/bin/env python

from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
  name='keep-presence',
  version='1.0.6',
  install_requires=install_requires,
  scripts=[
    'keep-presence.py',
  ]
)
