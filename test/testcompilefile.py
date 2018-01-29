from pytcc import TCC, FILE
comp = TCC(output_type=FILE)
comp.add_library_path("./")
comp.compile_file("program.c")
comp.output_file("program.exe")
