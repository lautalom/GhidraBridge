# @author lautalom
# @category layer


if __name__=='__main__':
    try:
        import importlib.util
        import cp
    except:
        import sys
        import os
        sys.path.append(os.path.dirname(__file__))
        print(sys.path)
        import cp
    finally:
        plugin = "analyser" 
        cp.currentProgram = currentProgram
        module = importlib.import_module(plugin)
        module.PLUGIN_ENTRY().run(0)
        print("Done")
