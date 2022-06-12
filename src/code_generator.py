'''This module generates java code from the parser tree'''

class Generator:
    '''
    This class generates java code from the parser tree that it gets as input.
    First it creates a command list from the tree.
    Then it pastes the commands from that list to a copy of the template.
    '''

    def __init__(self, tree):
        self.command_list = []
        self.tree = tree
        self.commands_dict = {
        "eteen": self.generate_move_forward, "forward": self.generate_move_forward,
        "taakse": self.generate_move_backward, "back": self.generate_move_backward,
        "oikealle": self.generate_rotate_right, "right": self.generate_rotate_right,
        "vasemmalle": self.generate_rotate_left, "left": self.generate_rotate_left,
        "tulosta": self.generate_show, "show": self.generate_show}

    def list_commands(self):
        '''This function creates the command list'''

        for child in self.tree.root.children:
            self.command_list.append(self.commands_dict[child.keyword](child.child.value))

    def generate_code(self): # pragma: no cover
        '''
        This function copies the commands from the command list
        and pastes them to a copy of the java template
        '''

        template = open("templates/JavaTemplate.java","r", encoding="utf-8")
        code = open("Main.java","w", encoding="utf-8")
        for line in template.readlines():
            if "// insert generated code here" in line:
                for command in self.command_list:
                    code.write("\t\t")
                    code.write(command)
                    code.write(";\n")
            else:
                code.write(line)
        template.close()
        code.close()

    @classmethod
    def generate_move_forward(cls, amount):
        '''This method returns the move forward command'''

        java_command = "travel(" + amount + ")"
        return java_command

    @classmethod
    def generate_move_backward(cls, amount):
        '''This method returns the move backward command'''

        amount = int(amount)*-1
        java_command = "travel(" + str(amount) + ")"
        return java_command

    @classmethod
    def generate_rotate_right(cls, amount):
        '''This method returns the rotate right command'''

        java_command = "rotate(" + amount + ")"
        return java_command

    @classmethod
    def generate_rotate_left(cls, amount):
        '''This method returns the rotate left command'''

        amount = int(amount)*-1
        java_command = "rotate(" + str(amount) + ")"
        return java_command

    @classmethod
    def generate_show(cls, message):
        '''This method returns the show command'''

        if message[0] == '"':
            message = message[1:]
        java_command = 'printToLCD("' + message + '")'
        return java_command
