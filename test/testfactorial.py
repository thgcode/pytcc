from ctypes import CFUNCTYPE, POINTER, c_int
from pytcc import TCC, MEMORY
comp = TCC()
comp.output_type = MEMORY
comp.add_library_path("./")
comp.add_file("factorial.c")
comp.relocate()
factorial = comp.get_symbol("factorial")
factorialsignature = CFUNCTYPE(c_int, c_int)
func = factorialsignature(factorial)
print(func(6)) # Returns the factorial of 6
