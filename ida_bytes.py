# module for IDA Plugin SDK API wrapper: bytes
# @author lautalom
# @category layer


"""module for IDA Plugin SDK API wrapper: bytes"""

from array import array
import ghidra_bridge
from jfx_bridge.bridge import BridgeTimeoutException


def get_bytes(start, length):
    """Returns length bytes from start of a segment"""
    print(f"Getting {length} bytes at {start}...", end="")
    timeout = 2
    possible = True
    if start == 0:
        return b""
    while possible:
        with ghidra_bridge.GhidraBridge(namespace=globals(), response_timeout=timeout):
            res = b""
            try:
                res = getBytes(toAddr(start), length + 1)
                res = res.tolist()
                res = [i if i >= 0 else (256 + i) for i in res]
                res = array("B", res)
                possible = False
                print("Success")
            except BridgeTimeoutException:
                print("Timed out, retrying...")
                timeout *= 2
            except Exception as ex:
                possible = False
                print(str(ex))
    return bytes(res)
