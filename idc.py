"""idc wrapper"""

from array import array
from ghidra.program.flatapi import FlatProgramAPI
import cp

SEGATTR_END = 8


def get_segm_attr(segea, attr):
    """
    Get segment attributes...
    @param segea: any address within segment
    @param attr: segment attributes as per ida config, define by need.
    """
    minAddress = cp.currentProgram.minAddress.getOffset()
    fcp = FlatProgramAPI(cp.currentProgram)
    if attr == SEGATTR_END:
        end =  cp.currentProgram.getMemory().getBlock(fcp.toAddr(segea+minAddress)).getEnd().getOffset()
        return end - minAddress


def GetString(address, length):
    """
    was ported to ida_bytes get_strlit_contents according to IDA
    address: linear address of the string
    length: length of the string in bytes including  null terminator
    return: a bytes-filled str object.
    """
    res = b""
    fcp = FlatProgramAPI(cp.currentProgram)
    try:
        res = fcp.getBytes(fcp.toAddr(address), length + 1)
        res = res.tolist()
        res = [i if i >= 0 else (256 + i) for i in res]
        res = array("B", res).tobytes()
    except Exception as ex:
        print("GetString failed: ", str(ex))
    finally:
        return res


def get_segm_name(ea):
    """
    @param ea: address
    returns: name of function's segment or empty string in case of failure
    """
    res = ""
    minAddress = cp.currentProgram.minAddress.getOffset()
    fcp = FlatProgramAPI(cp.currentProgram)
    try:
        res = cp.currentProgram.getMemory().getBlock(fcp.toAddr(ea+minAddress)).getName()
        if res == "EXTERNAL":
            res = "extern"
    except Exception as e:
        print("Failed to get segment", str(e))
    finally:
        return res


def get_func_name(func):
    minAddress = cp.currentProgram.minAddress.getOffset()
    fcp = FlatProgramAPI(cp.currentProgram)
    listing = cp.currentProgram.getListing()
    function = listing.getFunctionAt(fcp.toAddr(minAddress+func))
    return function.getName()
