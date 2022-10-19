# idc wrapper
# @category GCL

"""idc wrapper"""

from array import array
#from ghidra.program.database.mem.MemoryBlockDB import getBytes
from ghidra.program.flatapi import FlatProgramAPI
import cp

SEGATTR_END = 8


def get_segm_attr(segea, attr):
    """
    Get segment attributes...
    @param segea: any address within segment
    @param attr: segment attributes as per ida config, define by need.
    """
    if attr == SEGATTR_END:
        return (
            cp.currentProgram.getMemory().getBlock(FlatProgramAPI(cp.currentProgram).toAddr(segea)).getEnd().getOffset()
        )


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


def get_segm_name(func):
    """
    @param func: function object
    returns: name of function's segment or empty string in case of failure
    """
    res = ""
    try:
        res = str(
            cp.currentProgram.getMemory()
            .getBlock(FlatProgramAPI(cp.currentProgram).toAddr(func.getEntryPoint().getOffset()))
            .getName()
        )
        if res == "EXTERNAL":
            res = "extern"
    except Exception as e:
        print("Failed to get segment", str(e))
    finally:
        return res


def get_func_name(func):
    return func.getName()
