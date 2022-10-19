
# Description

This is a work in progress to integrate FLOSS plugins into Ghidra. 

The constraint is that plugins source code should not be modified. 

That implies wrapping every call made to the source code API with Ghidra's API. That has costs like different API versioning support depending on the plugin source code and sometimes...best approximation results (for example a particular function might not be available in Ghidra but a rather similar function might do the trick).

# Dependencies

- [Pyhidra](https://github.com/dod-cyber-crime-center/pyhidra).
- The dependencies of the plugin you will be using. 

# Usage with GUI

- Edit `invoke.py` with the name of the plugin's main file/entrypoint. 
- Add your plugin directory to Ghidra with Ghidra's Script Manager.
- Call `pyhidra -g` for GUI mode. 
- Add the layer files into the directory of the plugin.
- Run `invoke.py`. 

# Usage without GUI

- Edit `invoke.py` with the name of the plugin's main file/entrypoint. 
- Add your plugin directory to Ghidra with Ghidra's Script Manager.
- Call `pyhidra` for repl mode. 
- Add the layer files into the directory of the plugin.
- Run `pyhidra.run_script(r"BINARY_PATH",r"INVOKE.PY_PATH)"`.
# Supported Plugins

- [Findcrypt](https://github.com/polymorf/findcrypt-yara/blob/master/findcrypt3.py)
- [Syms2elf]
- [UEFI REtool]