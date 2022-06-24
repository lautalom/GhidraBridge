""" module for IDA High level utility functions"""
# module for IDA High level utility functions
# @lautalom
# @category layer
# @keybinding
# @menupath
# @toolbar

import ghidra_bridge


def Segments():
    """ returns a list of segments starting offsets """
    with ghidra_bridge.GhidraBridge(namespace=globals()):
        blocks = currentProgram.getMemory().getBlocks()
        ans = [
            i.getStart().getOffset() for i in blocks if i.getStart().getOffset() != 0]
        return ans
