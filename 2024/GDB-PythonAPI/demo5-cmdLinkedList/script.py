import gdb
class StudentListDumpCmd(gdb.Command):
    """Prints the StudentListNode from our example in a nice format!"""

    def __init__(self):
        super(StudentListDumpCmd, self).__init__(
            "student_list_dump", gdb.COMMAND_USER
        )

    def _student_list_to_str(self, val):
        idx = 0
        node_ptr = val
        result = ""
        while node_ptr != 0:
            student = node_ptr["student"]
            result += "\n%d: Student Name: %s, Student ID: %s, Student Age: %d" % (idx, student['name'], student['studentId'], student['age'])
            node_ptr = node_ptr["next"]
            idx += 1
        result = ("Found a Linked List with %d nodes:" % idx) + result
        return result

    def complete(self, text, word):
        return gdb.COMPLETE_SYMBOL

    def invoke(self, args, from_tty):
        # We can pass args here and use Python CLI utilities like argparse
        # to do argument parsing
        print("Args Passed: %s" % args)

        node_ptr_val = gdb.parse_and_eval(args)
        print(node_ptr_val.type)
        if str(node_ptr_val.type) != "StudentNode *":
            print("Expected pointer argument of type (StudentNode *)")
            return

        print(self._student_list_to_str(node_ptr_val))


StudentListDumpCmd()

