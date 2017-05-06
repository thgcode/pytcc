from pytcc import TCC, MEMORY
import sys
comp = TCC()
comp.output_type = MEMORY
comp.add_library_path("./")
comp.compile_string('''
int main(int argc, char **argv)
    {
    int i;
    for (i = 0; i < argc; i++)
        printf("%s", argv[i]);
    return 0;
}
''')
comp.run(sys.argv)
