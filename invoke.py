#TODO invoke findcrypt
#@author 
#@category findcrypt
#@keybinding 
#@menupath 
#@toolbar 

import ghidra_bridge
import importlib.util 

with ghidra_bridge.GhidraBridge(namespace=globals()) as b:
    plugin = input("Plugin Name: ")
    module = importlib.import_module(plugin)
    module.PLUGIN_ENTRY().run(0)
    #b.remote_shutdown()

