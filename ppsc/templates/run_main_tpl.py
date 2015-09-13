# -*- coding: utf-8 -*-


run_templates = """
# -*- coding: utf-8 -*-

import argparse

def run_main():
    run_parse = argparse.ArgumentParser(prog="{0}")
    run_parse.add_argument("--debug",help="debug mode on ,default off",type=bool)
    run_parse.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

    run_parse.parse_args()

"""
