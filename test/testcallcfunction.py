import sys
from pathlib import Path
from ctypes import *
from pytcc import TCC

source = '''
#include "Python.h"

PyObject * pop(PyObject * self, PyObject * args, PyObject * kwargs)
{
	return PyLong_FromLong(sum(2, square(2)));
}

int sum(int a, int b)
{
	return a + b;
}

int main(int argc, char **argv)
{
	printf("%s %d\n", argv[0], sum(2, 2));
	return 0;
}
'''

def square(n):
	return n ** 2

c_square = CFUNCTYPE(c_int, c_int)(square)

python_dir = Path(sys.executable).parent
comp = TCC()
comp.add_library_path(f'{python_dir}')
comp.add_include_path(f'{python_dir / "include"}')
comp.add_library('python37')
comp.add_symbol('square', c_square)
comp.compile_string(source)
comp.relocate()
pop = CFUNCTYPE(py_object)(comp.get_symbol('pop'))

print(pop())
