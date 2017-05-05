from ctypes import c_char_p, pointer
from pytcc import TCC, MEMORY
comp = TCC()
comp.output_type = MEMORY
comp.preprocessor_symbols[b"DEBUG"] = b"1"
comp.add_library_path(b"./")
comp.add_file(b"test.c")
comp.compile_string(b'''
int main(int argc, char **argv)
    {
    printf("%s %d", argv[0], sum(2, 2));
    return 0;
}
''')
comp.run(1, pointer(c_char_p(b"test")))
