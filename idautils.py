# idautils wrapper
# @author lautalom
# @category layer

""" IDA High level utility functions"""
import cp

def Segments():
    """returns a list of segments starting offsets"""
    blocks = cp.currentProgram.getMemory().getBlocks()
    ans = [
        i.getStart().getOffset() for i in blocks if i.getStart().getOffset() != 0
    ]
    return ans


def Functions(start=None, end=None):
    """
    Get a list of functions
    @param start: start address (default: inf.min_ea)
    @param end:   end address (default: inf.max_ea)
    @return: list of function entrypoints between start and end
    @note: The last function that starts before 'end' is included even
    if it extends beyond 'end'. Any function that has its chunks scattered
    in multiple segments will be reported multiple times, once in each segment
    as they are listed.
    """
    if start is None:
        start = cp.currentProgram.minAddress
    if end is None:
        end = cp.currentProgram.maxAddress
    
    chunk = cp.currentProgram.getFunctionManager().getFunctions(start, True)
    funcs = [f for f in chunk if f.getEntryPoint() < end]
    return funcs


class FunWrapper:
    def __init__(self, f):
        self.start_ea = f.getEntryPoint().getOffset()
        self.fsize = f.getBody().getNumAddresses()

    def size(self):
        return self.fsize


def get_func(f):
    func = FunWrapper(f)
    return func
