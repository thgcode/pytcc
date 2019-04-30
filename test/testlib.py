from pytcc import libtcc, FILE
state = libtcc.tcc_new()
libtcc.tcc_set_output_type(state, FILE)
libtcc.tcc_add_library_path(state, b".")
libtcc.tcc_compile_string(state, b'''
int main()
    {
    printf("Hello!");
    return 0;
}
''')
libtcc.tcc_output_file(state, b"a.exe")
libtcc.tcc_delete(state)
