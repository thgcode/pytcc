from pytcc import TCC, FILE
comp = TCC()
comp.output_type = FILE
comp.preprocessor_symbols[b"DEBUG"] = b"1"
comp.add_library_path(b"./")
comp.add_file(b"test.c")
comp.compile_string(b'''
int main()
    {
    printf("%d", sum(2, 2));
    return 0;
}
''')
comp.output_file(b"b.exe")
