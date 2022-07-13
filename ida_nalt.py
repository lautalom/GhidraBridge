# ida_nalt wrapper (syms2elf)
# @author lautalom
# @category layer

import ghidra_bridge

def get_input_file_path():
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        return currentProgram.getExecutablePath()