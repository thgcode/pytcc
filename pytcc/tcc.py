from ctypes import c_char_p
from ._libtcc import (lib, TCC_OUTPUT_MEMORY as MEMORY, TCC_OUTPUT_FILE as FILE,
    TCC_OUTPUT_OBJ as OBJ, TCC_OUTPUT_PREPROCESS as PREPROCESS, TCC_RELOCATE_AUTO as AUTO,
    error_func)
import sys

message = ""

@error_func
def on_error(userdata, tmessage):
        global message
        message = tmessage.decode(sys.getdefaultencoding())

def _bytes(string, encoding=sys.getdefaultencoding()):
    """Always returns a byte string."""
    if isinstance(string, bytes):
        return string
    else:
        return bytes(string, encoding)

class Error(Exception):
    pass

def ok_or_exception(func, *args, **kw):
    """A decorator that raizes an exception if the result of the call is
    nonzero."""
    def f(*args, **kw):
        result = func(*args, **kw)
        if result != 0:
            raise Error("Error in %s: %d: %s" % (func.__name__, result, message))
        return result
    return f

class _DefiningSymbolsDict(dict):
    """A dictionary that defines symbols in the TCC compiler."""
    def __init__(self, state):
        super(_DefiningSymbolsDict, self).__init__()
        self.state = state

    def __setitem__(self, item, value):
        super(_DefiningSymbolsDict, self).__setitem__(item, value)
        lib.tcc_define_symbol(self.state, _bytes(item), _bytes(value))

    def __delitem__(self, item):
        super(_DefiningSymbolsDict, self).__delitem__(item)
        lib.tcc_undefine_symbol(self.state, _bytes(item))

class TCC(object):
    """Represents a TCCState structure."""
    def __init__(self):
        self.state = lib.tcc_new()
        self._library_path = None
        self._output_type = None
        self.preprocessor_symbols = _DefiningSymbolsDict(self.state)
        lib.tcc_set_error_func(self.state, None, on_error)

    def __del__(self):
        return lib.tcc_delete(self.state)

    @property
    def library_path(self):
        return self._library_path

    @library_path.setter
    def library_path(self, path):
        self._library_path = path
        return lib.tcc_set_lib_path(self.state, _bytes(path))

    @ok_or_exception
    def add_include_path(self, path):
        return lib.tcc_add_include_path(self.state, _bytes(path))

    @ok_or_exception
    def add_sysinclude_path(self, path):
        return lib.tcc_add_sysinclude_path(self.state, _bytes(path))

    @ok_or_exception
    def add_file(self, path):
        return lib.tcc_add_file(self.state, _bytes(path))

    @ok_or_exception
    def compile_string(self, string):
        return lib.tcc_compile_string(self.state, _bytes(string))

    @property
    def output_type(self):
        return self.output_type

    @output_type.setter
    @ok_or_exception
    def output_type(self, type):
        self._output_type = type
        return lib.tcc_set_output_type(self.state, type)

    @ok_or_exception
    def add_library_path(self, path):
        return lib.tcc_add_library_path(self.state, _bytes(path))

    @ok_or_exception
    def add_library(self, library):
        return lib.tcc_add_library(self.state, _bytes(library))

    @ok_or_exception
    def add_symbol(self, symbol, value):
        return lib.tcc_add_symbol(self.state, _bytes(symbol), value)

    @ok_or_exception
    def output_file(self, path):
        return lib.tcc_output_file(self.state, _bytes(path))

    @ok_or_exception
    def _run(self, argc, argv):
        return lib.tcc_run(self.state, argc, argv)

    def run(self, argv=None):
        if argv is None:
            argv = []
        c_argc = len(argv)
        if argv:
            c_argv = (c_char_p * c_argc)(*[c_char_p(_bytes(x)) for x in argv])
        else:
            c_argv = None
        return self._run(c_argc, c_argv)

    @ok_or_exception
    def relocate(self, type=AUTO):
        return lib.tcc_relocate(self.state, type)

    def get_symbol(self, symbol):
        return lib.tcc_get_symbol(self.state, _bytes(symbol))
