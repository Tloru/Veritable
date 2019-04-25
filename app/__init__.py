from .configure import *
from .init import *
from .meta import *
from .run import *

def setup(args, args_len, env=True, run_meta=False):
    assert len(args) == 0
    meta([]) if run_meta else None
    return auto_env() if env else None
