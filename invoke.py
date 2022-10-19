# @author lautalom
# @category GCL

if __name__=='__main__':
    import importlib.util
    import cp
    plugin = "syms2elf"
    module = importlib.import_module(plugin)
    cp.currentProgram = currentProgram
    module.PLUGIN_ENTRY().run(0)
    print('Done')
