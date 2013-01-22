#!/usr/bin/env python

"""
Phil Adams http://philadams.net

Create a simple event poster. See README.txt for details.
"""

import logging
import json
import os
from pprint import pprint

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from PIL import Image


margins = (38, 38, 38, 38)  # TRBL; 72 ppi


def shrink(dim, margins=(38, 38, 38, 38)):
    """dim, an (x,y) tuple
    margins, a top-right-bottom-left tuple
    x` = x-(left+right); y` = y-(top+bottom)
    return shrunk (x`, y`)"""
    x, y = dim
    top, left, bottom, right = margins
    return (x - (left + right), y - (top + bottom))


def is_landscape(dim):
    """given dim, an (x,y) tuple, return True if x > y"""
    return dim[0] > dim[1]


def landscape(dim):
    """given dim, an (x,y) tuple, return (max(dim), min(dim))"""
    return (max(dim), min(dim))


def portrait(dim):
    """given dim, an (x,y) tuple, return (min(dim), max(dim))"""
    return (min(dim), max(dim))


def main():
    import argparse

    # populate and parse command line options
    desc = 'Generate fliers for circulation'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('src_img', help='source image')
    args = parser.parse_args()

    # logging config
    log_level = logging.WARNING  # default
    if args.verbose == 1:
        log_level = logging.INFO
    elif args.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)

    outfile = './gen/circular.pdf'

    # load config file
    with open('./config.json') as f:
        config = json.loads(f.read())

    # load image, and scale/fit to full size (infer orientation)
    img = Image.open(args.src_img)
    orientation = landscape
    if not is_landscape(img.size):
        orientation = portrait
    img_new_dim = shrink(orientation(LETTER))
    img = img.resize(map(int, img_new_dim))

    # TODO: draw text strings

    # filenames
    outdir, tmp = os.path.split(outfile)
    fname, ext = os.path.splitext(tmp)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    # create PDF doc with img
    img_tmp = os.path.join(outdir, fname + '.png')
    img.save(img_tmp)
    doc = canvas.Canvas(outfile,
                pagesize=orientation(LETTER))
    doc.drawImage(img_tmp, 38, 38)
    doc.save()


if '__main__' == __name__:
    main()
