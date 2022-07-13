# idc wrapper
# @lautalom
# @category layer
# @keybinding
# @menupath
# @toolbar

"""idc wrapper"""

from array import array
import ghidra_bridge

SEGATTR_END = 8


def get_segm_attr(segea, attr):
    """
    Get segment attributes...
    @param segea: any address within segment
    @param attr: segment attributes as per ida config, define by need.
    """
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        if attr == SEGATTR_END:
            return currentProgram.getMemory().getBlock(toAddr(segea)).getEnd().getOffset()

def GetString(address, length):
    """
    address: linear address of the string
    length: length of the string in bytes including  null terminator
    return: a bytes-filled str object.
    """
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        res = b""
        try:
            res = getBytes(toAddr(address), length + 1)
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
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        res = ""
        try:
            res = str(
                currentProgram.getMemory()
                .getBlock(toAddr(func.getEntryPoint().getOffset()))
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
