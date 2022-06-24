#TODO invoke findcrypt
#@author 
#@category findcrypt
#@keybinding 
#@menupath 
#@toolbar 

import ghidra_bridge

from findcrypt3 import *

with ghidra_bridge.GhidraBridge(namespace=globals()) as b:
    a = PLUGIN_ENTRY()
    a.search()
    b.remote_shutdown()

