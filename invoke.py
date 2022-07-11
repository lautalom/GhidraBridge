# @author lautalom
# @category layer

if __name__=='__main__':
    try:
        import syms2elf
    except:
        import sys
        import os
        sys.path.append(os.path.dirname(__file__))
        print(sys.path)
    # plugin = input("Plugin Name: ")
    import importlib.util
    plugin = "syms2elf"
    module = importlib.import_module(plugin)
    try:
        module.PLUGIN_ENTRY().run(0)
    except Exception as e:
        print(e)
    finally:
        print("Done")
# a = syms2elf.PLUGIN_ENTRY()
# a.run(0)
# b.remote_shutdown()
