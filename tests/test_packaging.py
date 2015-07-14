#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    tests.test_packaging
    ~~~~~~~~~~~~~~~~~~~~

    This module tests the pypc packaging pipeline

    :copyright: (c) 2015 by Mek.
    :license: see LICENSE for more details.
"""

import sys
import os.path
import unittest

from pypc.create import Package

VALID_PKGNAME = 'foo'
VALID_PATH = os.path.expanduser('~')

ERR = {
    'invalid-basename': 'Package instantiation requires non-empty basename',
    'failed-instantiation': 'Package path incorrectly set'
}

class TestPackage(unittest.TestCase):

    def test_creation(self):
        p = Package(VALID_PKGNAME, path=VALID_PATH)
        self.assertTrue(p.path == VALID_PATH, ERR['failed-instantiation'])

    def test_generation(self):
        """Generation (i.e. Package(PATH).new()) tests should use
        a tempfile directory path.
        """
        pass
