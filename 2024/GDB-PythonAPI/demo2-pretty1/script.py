# pp.py

class FruitPrinter(object):
    def __init__(self, val):
        self.val = val

    def to_string (self):
        fruit = self.val['fruit']
        
        if (fruit == 0):
            name = "Orange"
        elif (fruit == 1):
            name = "Apple"
        elif (fruit == 2):
            name = "Banana"
        else:
            name = "unknown"
        return "Our fruit is " + name

def lookup_type (val):
    if str(val.type) == 'Fruit':
        return FruitPrinter(val)
    return None

# gdb.pretty_printers.append (lookup_type)

import gdb.printing
pp = gdb.printing.RegexpCollectionPrettyPrinter('Fruit')
pp.add_printer('Fruit', '^Fruit$', FruitPrinter)
gdb.printing.register_pretty_printer(gdb.current_objfile(), pp, replace=True)

