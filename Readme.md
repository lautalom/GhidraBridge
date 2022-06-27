
# Description

This is a work in progress to integrate IDA plugins into Ghidra. 

The constraint is that plugins source code should not be changed. That implies wrapping every processing call made to IDA's API with Ghidra's API on a by-need basis, ignoring  coding conventions (eg. giving less precedence to a module or function that is not needed for main plugin functionality, using whatever naming conventions each particular plugin uses, defining API already-deprecated methods), and sometimes...best effort choices. As you see, limitations are both given by IDA's and Ghidra's APIs, by the coding practices that authors of plugins follow, among others. 

# Dependencies

- [Ghidra Bridge](https://github.com/justfoxing/ghidra_bridge) is used to integrate Python 3 and some Python modules that are needed and are not builtin in Ghidra. The choice was either writting Python 2.7 as per Ghidra's current Jython support or developping Python 3 and removing Ghidra Bridge whenever Python 3 support was available (with or without Jython). The choice was not difficult.
- The dependencies of the plugin you will be using. 

# Usage with scripting

- Add your IDA plugin directory to Ghidra with the scripting manager. 
- (Optional) For ease of usage, you may want to add a line `#@category plugin_name` to each plugin file. This will show a directory in the script manager with all the plugin files. Technically the source code would be changing, but it's also not a need, just visually convenient.
- Add the layer files into the directory of the plugin. Make sure the plugin is supported, ask for support or add the support yourself!
- Either run Ghidra Bridge from ghidras UI or use headless analysis.

# Headless analysis example

## First time
So the first time ghidra imports a binary, it creates a project and saves some information about it. For details, you should check [this article](https://static.grumpycoder.net/pixel/support/analyzeHeadlessREADME.html#general). Run within GhidraRoot/support
the command `./analyzeHeadless <project_location> <project_name> -import <target_binary> -scriptPath <ghidra_bridge_script_path> -postscript <ghidra_bridge_server.py_location>`

## Every other time

Add the overwrite flag, keep all the previous parameters.

`./analyzeHeadless <project_location> <project_name> -import <target> -scriptPath <ghidra_bridge_script_path> -postscript <ghidra_bridge_server_location> -overwrite`

# Supported Plugins

- [Findcrypt](https://github.com/polymorf/findcrypt-yara/blob/master/findcrypt3.py)