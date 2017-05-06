from pytcc import TCC, FILE
comp = TCC()
comp.output_type = FILE
comp.preprocessor_symbols["DEBUG"] = "1"
comp.add_library_path("./")
comp.add_file("test.c")
comp.compile_string('''
int main()
    {
    printf("%d", sum(2, 2));
    return 0;
}
''')
comp.output_file("b.exe")
