# @category layer


if __name__ == '__main__':
    try:
        import importlib.util
        import cp
    except:
        import sys
        import os
        sys.path.append(os.path.join(os.path.dirname(__file__)))
        # sys.path.append(os.path.join(os.path.dirname(__file__),'uefi_analyser'))
        import cp
        print(sys.path)
    finally:
        plugin = "uefi_analyser"
        cp.currentProgram = currentProgram
        path = os.path.dirname(__file__)+'/'+plugin+'.py'
        spec = importlib.util.spec_from_file_location(plugin,path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # importlib.import_module(plugin)
        module.PLUGIN_ENTRY().run(0)
        print("Done")
