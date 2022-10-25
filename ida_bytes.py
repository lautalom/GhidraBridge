# module for IDA Plugin SDK API wrapper: bytes
# @category GCL


"""module for IDA Plugin SDK API wrapper: bytes"""

from array import array
import cp
from ghidra.program.flatapi import FlatProgramAPI
from idaapi import BADADDR


def get_bytes(start, length):
    """Returns length bytes from start of a segment"""
    res = b""
    minAddress = cp.currentProgram.minAddress.getOffset()
    start += minAddress
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
    that is greater than ea."""
    fcp = FlatProgramAPI(cp.currentProgram)
    listing = cp.currentProgram.getListing()
    minAddress = cp.currentProgram.minAddress.getOffset()
    codeUnit = listing.getCodeUnitAfter(
        fcp.toAddr(minAddress+ea))
    if maxea != cp.currentProgram.maxAddress.getOffset():
        if codeUnit.getAddress().getOffset() > maxea+cp.currentProgram.minAddress.getOffset():
            return int(BADADDR, 16)
    else:
        if codeUnit.getAddress().getOffset() > maxea:
            return int(BADADDR, 16)
    reladdr = int(codeUnit.getAddressString(False, False), 16)
    return reladdr - minAddress


def del_items(ea, flags=0, nbytes=1, may_destroy=None):
    pass


def create_struct(ea, length, tid, force=False):
    pass


def get_wide_byte(ea):
    return get_bytes(ea, 1)


def get_wide_word(ea):
    return get_bytes(ea, 2)


def get_wide_dword(ea):
    return get_bytes(ea, 4)


def set_cmt(ea, comm, rptble):
    fcp = FlatProgramAPI(cp.currentProgram)
    listing = cp.currentProgram.getListing()
    minAddress = cp.currentProgram.minAddress.getOffset()
    listing.setComment(fcp.toAddr(ea+minAddress), 1, comm)
