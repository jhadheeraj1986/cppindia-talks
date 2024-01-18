import gdb

class SimpleGDBDemo(gdb.Command):
    def __init__(self):
        super(SimpleGDBDemo, self).__init__("simple_demo", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        # Print the values of two variables
        var1_value = gdb.parse_and_eval('var1')
        var2_value = gdb.parse_and_eval('var2')

        print("Variable 1: {}".format(var1_value))
        print("Variable 2: {}".format(var2_value))

        # Set a breakpoint at a specific line
        gdb.Breakpoint('main.cpp:10')
        gdb.execute('continue')

# Register the command
SimpleGDBDemo()
