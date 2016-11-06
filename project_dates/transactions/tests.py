#!/usr/bin/python
# -*- coding: utf8 -*-
"""

Thanks to:

- pendulum/tests/test_create_from_format.py

"""

from django.test import TestCase

# Create your tests here.


def test_format():
	"""Test a use case"""
    p = Pendulum.create_from_format('2016-11-06', '%Y-%m-%d', 'UTC')
    assert p.timezone_name == 'UTC'
