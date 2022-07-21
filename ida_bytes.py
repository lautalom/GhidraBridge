# module for IDA Plugin SDK API wrapper: bytes
# @author lautalom
# @category layer


"""module for IDA Plugin SDK API wrapper: bytes"""

from array import array
from ghidra.program.database.mem.MemoryBlockDB import getBytes
from ghidra.program.flatapi import toAddr

def get_bytes(start, length):
    """Returns length bytes from start of a segment"""
    possible = True
    if start == 0:
        return b""
    while possible:
        res = b""
        try:
            res = getBytes(toAddr(start), length + 1)
            res = res.tolist()
            res = [i if i >= 0 else (256 + i) for i in res]
            res = array("B", res)
            possible = False
            print("Success")
        except Exception as ex:
            possible = False
            print(str(ex))
    return bytes(res)
