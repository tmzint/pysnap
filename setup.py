__author__ = 'timo merlin zint'

import sys
from setuptools import setup
# you may need setuptools instead of distutils

try:
    import Xlib.display, gtk
except:
    print ''
    print 'pysnap requires python-xlib and python-gtk'
    sys.exit(0)

setup(
    # basic stuff here
    scripts = [
        'pysnap.py'
    ]
)