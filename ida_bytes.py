# module for IDA Plugin SDK API wrapper: bytes
# @author lautalom
# @category layer


"""module for IDA Plugin SDK API wrapper: bytes"""

from array import array
import cp
from ghidra.program.database.mem.MemoryBlockDB import getBytes
from ghidra.program.flatapi import FlatProgramAPI

def get_bytes(start, length):
    """Returns length bytes from start of a segment"""
    res = b""
    try:
        res = FlatProgramAPI(cp.currentProgram).getBytes(FlatProgramAPI(cp.currentProgram).toAddr(start), length + 1)
        res = list(res)
        res = [i if i >= 0 else (256 + i) for i in res]
        res = array("B", res)
    except Exception as ex:
        print("Could not get bytes",str(ex))
    return bytes(res)
