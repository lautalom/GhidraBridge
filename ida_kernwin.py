# ida_kernwin wrapper (syms2elf)
# @author lautalom
# @category layer

import ghidra_bridge

def ask_form(*args):
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        return askYesNo("Continue?",args[0])
