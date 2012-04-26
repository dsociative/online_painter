# coding: utf8

from unittest.case import TestCase


class ZTest(TestCase):

    def __init__(self, *a, **kw):
        TestCase.__init__(self, *a, **kw)

        self.eq = self.assertEqual
        self.isinstance = self.assertIsInstance
        self.isfalse = self.assertFalse
