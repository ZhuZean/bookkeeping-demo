""" Imports every module from this directory

    Alembic can detect changes in any model inside this directory.
"""

import glob
from os.path import dirname
from os.path import basename
from os.path import isfile
from os.path import join

__all__ = [
    basename(f)[:-3]
    for f
    in glob.glob(join(dirname(__file__), "*.py"))
    if isfile(f) and not f.endswith('__init__.py')
]
