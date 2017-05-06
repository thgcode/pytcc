from ctypes import c_char_p, pointer
from pytcc import TCC, MEMORY
comp = TCC()
comp.output_type = MEMORY
comp.preprocessor_symbols["DEBUG"] = "1"
comp.add_library_path("./")
comp.add_file("test.c")
comp.compile_string('''
int main(int argc, char **argv)
    {
    printf("%s %d", argv[0], sum(2, 2));
    return 0;
}
''')
comp.run(1, pointer(c_char_p(b"test")))
