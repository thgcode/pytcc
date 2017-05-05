from pytcc import libtcc
state = libtcc.tcc_new()
libtcc.tcc_set_output_type(state, 1)
libtcc.tcc_add_library_path(state, b".")
libtcc.tcc_compile_string(state, b'''
void main()
    {
    printf("Hello!");
    return 0;
}
''')
libtcc.tcc_output_file(state, b"a.exe")
libtcc.tcc_delete(state)
