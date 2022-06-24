# ida_diskio wrapper
# @lautalom
# @category layer
# @keybinding
# @menupath
# @toolbar

"""ida_diskio wrapper"""

import ghidra_bridge


def get_user_idadir():
    """return path to IDA directory"""
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        idir = ghidra.GhidraApplicationLayout().getExtensionInstallationDirs()
        path_to_version = "IDAPro/Python/7xx"
        path = (
            str(idir[1]) + path_to_version if len(idir) > 0 else str(idir[0]) + path_to_version
        )
        return path
