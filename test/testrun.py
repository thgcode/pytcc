from pytcc import TCC
comp = TCC()
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
comp.run(["test"])
