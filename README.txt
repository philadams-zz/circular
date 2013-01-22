Circular (grf-tools)
====================

circular: a printed ad, directive, or notice intended for mass distribution.

Given an image and some text strings in `config.json`, create a circular 
with the image as a full-page background, and the text strings overlaid.

usage
-----

`python -h` has details. But essentially edit `config.json` and then run `python circular.py <src/img.jpg>`; your generated circular will be at `./gen/circular.pdf`. An example output file is in the `examples` directory.

future
------

- add --outfile option
- fix license - MIT?
- handle .jpg, .gif, etc.
- portrait/landscape switch
- align text right/left
