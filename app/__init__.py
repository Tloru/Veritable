from .configure import *
from .init import *
from .meta import *
from .routes import *
from .run import *

try: env = auto_env()
except: print("A Veritable Project does not exist in this folder...")
