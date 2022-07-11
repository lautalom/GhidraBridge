# ida_diskio wrapper (findcrypt)
# @author lautalom
# @category layer

"""ida_diskio wrapper"""

import ghidra


def get_user_idadir():
    """return path to IDA directory"""
    idir = ghidra.GhidraApplicationLayout().getExtensionInstallationDirs()
    path_to_version = "IDAPro/Python/7xx"
    path = (
        str(idir[1]) + path_to_version
        if len(idir) > 0
        else str(idir[0]) + path_to_version
    )
    return path
