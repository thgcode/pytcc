from ctypes import *
from ctypes.util import find_library
import os
import platform
import sys

# libtcc DLL handle
if sys.platform == 'linux' or sys.platform == 'darwin':
	ext = 'so'
elif sys.platform == 'win32':
	ext = 'dll'

try:
	lib = ctypes.cdll.LoadLibrary(f'libtcc.{ext}')
except OSError:
	raise Exception(
		f'Could not find libtcc.{ext} in path. Either add '
		f'TCC directory to path or CD into the folder containing libktcc.{ext}'
	)
except ImportError:
	raise Exception(
		'LibTCC was not compiled with the same architecture as this running '
		'Python process. Either reinstall Python or TCC.'
	)


class TCCState(Structure):
    pass

TCCState = POINTER(TCCState)
lib.tcc_new.restype = TCCState
lib.tcc_delete.restype = None
lib.tcc_delete.argtypes = [TCCState]
lib.tcc_set_lib_path.restype = None
lib.tcc_set_lib_path.argtypes = [TCCState, c_char_p]
error_func = CFUNCTYPE(None, c_void_p, c_char_p)
lib.tcc_set_error_func.restype = None
lib.tcc_set_error_func.argtypes = [TCCState, c_void_p, error_func]
lib.tcc_set_options.restype = c_int
lib.tcc_set_options.argtypes = [TCCState, c_char_p]
lib.tcc_add_include_path.restype = c_int
lib.tcc_add_include_path.argtypes = [TCCState, c_char_p]
lib.tcc_add_sysinclude_path.restype = c_int
lib.tcc_add_sysinclude_path.argtypes = [TCCState, c_char_p]
lib.tcc_define_symbol.restype = c_int
lib.tcc_define_symbol.argtypes = [TCCState, c_char_p, c_char_p]
lib.tcc_undefine_symbol.argtypes = [TCCState, c_char_p]
lib.tcc_undefine_symbol.restype = c_int
lib.tcc_add_file.argtypes = [TCCState, c_char_p]
lib.tcc_add_file.restype = c_int
lib.tcc_compile_string.argtypes = [TCCState, c_char_p]
lib.tcc_compile_string.restype = c_int
lib.tcc_set_output_type.argtypes = [TCCState, c_int]
lib.tcc_set_output_type.restype = c_int

TCC_OUTPUT_MEMORY = 1
TCC_OUTPUT_FILE = 2
TCC_OUTPUT_DLL = 3
TCC_OUTPUT_OBJ = 4
TCC_OUTPUT_PREPROCESS = 5

lib.tcc_add_library_path.argtypes = [TCCState, c_char_p]
lib.tcc_add_library_path.restype = c_int
lib.tcc_add_library.argtypes = [TCCState, c_char_p]
lib.tcc_add_library.restype = c_int
lib.tcc_add_symbol.argtypes = [TCCState, c_char_p, c_void_p]
lib.tcc_add_symbol.restype = c_int

lib.tcc_output_file.argtypes = [TCCState, c_char_p]
lib.tcc_output_file.restype = c_int
lib.tcc_run.argtypes = [TCCState, c_int, POINTER(c_char_p)]
lib.tcc_run.restype = c_int
lib.tcc_relocate.argtypes = [TCCState, c_void_p]
lib.tcc_relocate.restype = c_int

TCC_RELOCATE_AUTO = c_void_p(1)
lib.tcc_get_symbol.argtypes = [TCCState, c_char_p]
lib.tcc_get_symbol.restype = c_void_p
