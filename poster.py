#!/usr/bin/env python

"""
Phil Adams http://philadams.net

Create a simple event poster. See README.txt for details.
"""

import logging


def main():
    import argparse

    # populate and parse command line options
    parser = argparse.ArgumentParser(description='Image archiving for VERA+')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='count', default=0)
    group.add_argument('-q', '--quiet', action='store_true')
    args = parser.parse_args()

    # logging config
    log_level = logging.WARNING  # default
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)


if '__main__' == __name__:
    main()
