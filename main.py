# @category GCL


if __name__ == '__main__':
    try:
        import importlib.util
        import sys
        import os
        import cp
    except:
        sys.path.append(os.path.dirname(__file__))
        import cp
    finally:
        plugin = "findcrypt3"
        cp.currentProgram = currentProgram
        path = os.path.dirname(__file__)+'/'+plugin+'.py'
        spec = importlib.util.spec_from_file_location(plugin,path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.PLUGIN_ENTRY().run(0)
        print("Done")
