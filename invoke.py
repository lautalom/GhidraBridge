# @author lautalom
# @category layer

if __name__=='__main__':
    try:
        import cp
    except:
        import sys
        import os
        sys.path.append(os.path.dirname(__file__))
        import cp
        print(sys.path)
    finally:
        plugin = input("Plugin Name: ")
        import importlib.util
        module = importlib.import_module(plugin)
        cp.currentProgram = currentProgram
        module.PLUGIN_ENTRY().run(0)
        print("Done")
