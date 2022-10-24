# idautils wrapper
# @category GCL

""" IDA High level utility functions"""
from uefi_analyser import cp

def Segments():
    """returns a list of segments starting offsets"""
    blocks = cp.currentProgram.getMemory().getBlocks()
    minAddress = cp.currentProgram.minAddress.getOffset()
    ans = [
        i.getStart().getOffset()-minAddress for i in blocks if i.getStart().getOffset() != 0
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
    minAddress = cp.currentProgram.minAddress.getOffset()
    if start is None:
        start = cp.currentProgram.minAddress
    if end is None:
        end = cp.currentProgram.maxAddress
    
    chunk = cp.currentProgram.getFunctionManager().getFunctions(start, True)
    funcs = [f.getEntryPoint().getOffset()-minAddress for f in chunk if f.getEntryPoint() < end]
    return funcs


class FunWrapper:
    def __init__(self, f):
        minAddress = cp.currentProgram.minAddress.getOffset()
        listing = cp.currentProgram.getListing()
        function = listing.getFunctionAt(minAddress+f)
        self.start_ea = function.getEntryPoint().getOffset()
        self.fsize = function.getBody().getNumAddresses()

    def size(self):
        return self.fsize


def get_func(f):
    func = FunWrapper(f)
    return func
