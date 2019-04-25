from . import *

import os
from distutils.dir_util import copy_tree

def init(args):
    # checking args
    assert len(args) <= 1
    path = "" if len(args) == 0 else args[0]

    veritable_path = get_veritable_path()
    project_path = join(os.getcwd(), path)

    copy_tree(join(veritable_path, "base"), project_path)
