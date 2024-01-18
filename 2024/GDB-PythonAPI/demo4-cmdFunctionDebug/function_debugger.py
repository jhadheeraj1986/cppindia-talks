import gdb

class FunctionDebugger(gdb.Command):
    def __init__(self):
        super(FunctionDebugger, self).__init__("function_debug", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        if not arg:
            print("Usage: function_debug <function_name>")
            return

        function_name = arg

        # Set a breakpoint at the function entry point
        breakpoint_location = function_name
        gdb.Breakpoint(function=breakpoint_location)
        gdb.execute('continue')
        print("Breakpoint set at the entry point of function '{}'".format(function_name))

    

# Register the command
FunctionDebugger()
