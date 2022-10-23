# module for IDA Plugin SDK API wrapper: bytes
# @author lautalom
# @category layer


"""module for IDA Plugin SDK API wrapper: bytes"""

from array import array
import uefi_analyser.cp as cp
from ghidra.program.database.mem.MemoryBlockDB import getBytes
from ghidra.program.flatapi import FlatProgramAPI
from idaapi import BADADDR


def get_bytes(start, length):
    """Returns length bytes from start of a segment"""
    res = b""
    start += cp.currentProgram.minAddress.getOffset()
    try:
        res = FlatProgramAPI(cp.currentProgram).getBytes(
            FlatProgramAPI(cp.currentProgram).toAddr(start), length + 1)
        res = list(res)
        res = [i if i >= 0 else (256 + i) for i in res]
        res = array("B", res)
    except:
        print("Could not get bytes")
    return bytes(res)


def next_head(ea, maxea):
    """get the next code unit that starts at an address 
    that is greater than the given address (ea)."""
    fcp = FlatProgramAPI(cp.currentProgram)
    listing = cp.currentProgram.getListing()
    codeUnit = listing.getCodeUnitAfter(
        fcp.toAddr(cp.currentProgram.minAddress.getOffset()+ea))
    if codeUnit is None:
        return int(BADADDR,16)
    elif codeUnit.getAddress().getOffset() > maxea:
        #maxea is an absolute address
        return int(BADADDR, 16)
    reladdr = int(codeUnit.getAddressString(False, False), 16)
    return reladdr - cp.currentProgram.minAddress.getOffset()


def del_items(ea, flags=0, nbytes=1, may_destroy=None):
    pass

def create_struct(ea, length, tid, force=False):
    pass

def get_wide_word(ea):
    return get_bytes(ea, 2)

def get_wide_dword(ea):
    return get_bytes(ea, 4)