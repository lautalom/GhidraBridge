# ida_kernwin wrapper (syms2elf)
# @author lautalom
# @category layer
<<<<<<< HEAD
import ghidra_bridge

def ask_form(*args):
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        return askYesNo("Continue?", args[0])
=======

def ask_form(*args):
    return askYesNo("Continue?", args[0])
>>>>>>> pyhidra
