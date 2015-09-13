# -*- coding: utf-8 -*-

import unittest
import sys
import os

try:
    import ppsc.tests
except :
    sys.path.append("../../")
    try:
        import ppsc.tests
    except:
        raise

from ppsc.makedirs.ppsc_tree import PpscTree


class TestMakedirsPpscTree(unittest.TestCase):
    def setUp(self):
        self.ppsc = PpscTree(project_name="test")
    def test_ppsc_tree_args1(self):
        self.ppsc.make_tree()
    def test_ppsc_tree_args2(self):
        self.ppsc.make_init_files()

if __name__ == '__main__':
    unittest.main()
