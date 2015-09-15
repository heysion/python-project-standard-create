# -*- coding: utf-8 -*-

import os
import pdb
class PpscTree:
    def __init__(self,project_name,app_name=None):
        self._root_path = project_name
        self._app_path = self._root_path + "/" + (app_name if app_name else project_name)
        self._test_path = self._app_path + "/tests"
        self._docs_path = self._root_path + "/docs"

    def make_tree(self):
        if not os.path.exists(self._test_path):
            os.makedirs(self._test_path)
        if not os.path.exists(self._docs_path):
            os.makedirs(self._docs_path)
        if not os.path.exists(self._app_path):
            os.makedirs(self._app_path)
        if not os.path.exists(self._root_path):
            os.makedirs(self._root_path)

    def make_init_files(self):
        init_file_name = "/__init__.py"
        if not os.path.exists(self._app_path+init_file_name):
            os.mknod(self._app_path+init_file_name)
        if not os.path.exists(self._test_path+init_file_name):
            os.mknod(self._test_path+init_file_name)

