# @author lautalom
# @category layer

if __name__=='__main__':
    try:
        import cp
        import syms2elf
    except:
        import sys
        import os
        sys.path.append(os.path.dirname(__file__))
        import cp
        import syms2elf
        print(sys.path)
    finally:
        # plugin = input("Plugin Name: ")
        import importlib.util
        plugin = "syms2elf"
        module = importlib.import_module(plugin)
        cp.currentProgram = currentProgram
        try:
            print(cp.currentProgram.minAddress, 'master!')
            module.PLUGIN_ENTRY().run(0)
        except Exception as e:
            print(str(e), type(e).__name__)
        finally:
            print("Done")
# a = syms2elf.PLUGIN_ENTRY()
# a.run(0)
# b.remote_shutdown()
