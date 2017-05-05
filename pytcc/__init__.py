from .version import VERSION, BUNDLED_TCC_VERSION
from ._libtcc import lib as libtcc
from .tcc import TCC, MEMORY, FILE, OBJ, PREPROCESS
__all__ = ["libtcc", "TCC", "VERSION", "BUNDLED_TCC_VERSION"]
