
class Generator:
    def __init__(self, tree):
        self.command_list = []
        self.tree = tree
        self.commands_dict = {
        "eteen": self.generate_move_forward, "forward": self.generate_move_forward,
        "taakse": self.generate_move_backward, "back": self.generate_move_backward,
        "oikealle": self.generate_rotate_right, "right": self.generate_rotate_right,
        "vasemmalle": self.generate_rotate_left, "left": self.generate_rotate_left,
        "tulosta": self.generate_show, "show": self.generate_show}
        self.list_commands()
        self.generate_code()

    def list_commands(self):
        for child in self.tree.root.children:
            self.command_list.append(self.commands_dict[child.keyword](child.child.value))

    def generate_code(self):
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
        java_command = "moveForward(" + str(amount) + ")"
        return java_command

    @classmethod
    def generate_move_backward(cls, amount):
        java_command = "moveBackward(" + str(amount) + ")"
        return java_command

    @classmethod
    def generate_rotate_right(cls, amount):
        java_command = "rotate(" + str(amount) + ")"
        return java_command

    @classmethod
    def generate_rotate_left(cls, amount):
        java_command = "rotate(" + str(amount) + ")"
        return java_command

    @classmethod
    def generate_show(cls, message):
        java_command = 'printToLCD("' + str(message) + '")'
        return java_command
