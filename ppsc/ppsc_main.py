# -*- coding: utf-8 -*-

import argparse

from templates.run_main_tpl import run_templates
def run_main():
    run_parse = argparse.ArgumentParser(prog="ppsc")
    run_parse.add_argument("--debug",help="debug mode on ,default off",type=bool)
    run_parse.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

    run_parse.parse_args()

if __name__ == "__main__":
    print run_templates.format("app")

