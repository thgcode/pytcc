from pytcc import TCC
import sys
comp = TCC()
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
