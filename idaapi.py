
"""idaapi wrapper"""

# idaapi wrapper
# @lautalom
# @category layer
# @keybinding
# @menupath
# @toolbar

import ghidra_bridge
from os import getcwd, path

SN_NOCHECK = hex(00)  # Replace invalid chars with SUBSTCHAR
BWN_DISASM = 0
AST_ENABLE_FOR_WIDGET = 2
AST_DISABLE_FOR_WIDGET = 3
PLUGIN_KEEP = 2
PLUGIN_UNL = 8
PLUGIN_OK = 1
SETMENU_APP = 1


def action_desc_t(*args):
    """unused"""
    return args[0]


class action_handler_t:
    """unused"""

    def __init__(self):
        return


class Choose:
    """unused"""

    CHCOL_HEX = 0
    CHCOL_PLAIN = 0

    def __init__(*args, **kwargs):
        return

    def Show(self):
        """print results of search"""
        print(self.items)
        return True


class plugin_t:
    """unused"""

    def __init__(self):
        self.init()


def register_action(*args):
    """unused"""
    print("called register_action", args)


def unregister_action(*args):
    """unused"""
    print("Called unregister_action:", args)


def attach_action_to_menu(*args):
    """unused"""
    print("Called attach_action_to_menu:", args)


def set_name(l_addr, name, flags=SN_NOCHECK):
    """Rename an address
    @param l_addr - linear address
    @param name - new name of address. If name == "", then delete old name
    @param flags - combination of SN_... constants
    """
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        if hex(flags) == SN_NOCHECK:
            currentProgram.listing.setComment(toAddr(l_addr), 1, name)


# currently in ida kernwin
class Form:
    """mock form as needed by syms2elf"""
    def __init__(self, form, controls):
        self.form = form
        self.txtFile = self.txtfile(0, path.join(controls["txtFile"], "symbols.elf"))

    class txtfile:
        def __init__(self, id, value):
            self.id = id
            self.value = value

    def GetControlValue(*args):
        return

    def SetControlValue(file):
        return file

    def FormChangeCb(cfunc):
        return cfunc

    def FileInput(**kwargs):
        return getcwd()

    def Compile(self):
        print("HI THERE")
        return True

    def Compiled(self):
        return False

    def Execute(*args):
        return 1

    def Free(self):
        return


def get_file_type_name():
    """returns the format of an executable file"""
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        return str(currentProgram.getExecutableFormat())



def warning(*args):
    """defined only for sake of completeness with syms2elf"""
    print(*args)
