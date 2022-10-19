# module for IDA Plugin SDK API wrapper: bytes
# @author lautalom
# @category layer


"""module for IDA Plugin SDK API wrapper: bytes"""

from array import array
#from ghidra.program.database.mem.MemoryBlockDB import getBytes
from ghidra.program.flatapi import FlatProgramAPI
from ghidra.program.model.mem import MemoryAccessException
import cp
import sys


def get_bytes(start, length):
    """Returns length bytes from start of a segment"""
    res = bytearray(length+1)
    fcp = FlatProgramAPI(cp.currentProgram)
    try:
        res = fcp.getBytes(fcp.toAddr(start), length + 1)
        res = list(res)
        res = [i if i >= 0 else (256 + i) for i in res]
        res = array("B", res)
    except MemoryAccessException as ex:
        print(str(ex))
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        return res
