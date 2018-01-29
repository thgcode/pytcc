from ctypes import c_int, CFUNCTYPE, POINTER
from pytcc import TCC
comp = TCC()
comp.preprocessor_symbols["DEBUG"] = "1"
comp.add_library_path("./")

def square(n):
    return n ** 2

squaresignature = CFUNCTYPE(c_int, c_int)
func = squaresignature(square)

comp.add_symbol("square", func)
comp.compile_string('''
int main(int argc, char **argv)
    {
    printf("%d", square(6));
    return 0;
}
''')
comp.run()
