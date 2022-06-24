
"""idaapi wrapper"""

# idaapi wrapper
# @lautalom
# @category layer
# @keybinding
# @menupath
# @toolbar

import ghidra_bridge

SN_NOCHECK = hex(00)  # Replace invalid chars with SUBSTCHAR
BWN_DISASM = 0
AST_ENABLE_FOR_WIDGET = 2
AST_DISABLE_FOR_WIDGET = 3
PLUGIN_KEEP = 1
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
        if flags == SN_NOCHECK:
            currentProgram.listing.setComment(toAddr(l_addr), 1, name)
