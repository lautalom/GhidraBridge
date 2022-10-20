# @category GCL

if __name__=='__main__':
    import importlib.util
    import cp
    plugin = "findcrypt3"
    module = importlib.import_module(plugin)
    cp.currentProgram = currentProgram
    module.PLUGIN_ENTRY().run(0)
    module.p_initialized = False
    print('Done')
