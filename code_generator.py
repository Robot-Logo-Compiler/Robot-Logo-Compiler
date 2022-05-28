
class Generator:
    def __init__(self, tree):
        self.command_list = []
        self.tree = tree
        self.list_commands()
        self.generate_code()

    def list_commands(self):
        for child in self.tree.root.children:
            if child.keyword == "eteen":
                command = "moveForward(" + str(child.child.value) + ")"
                self.command_list.append(command)
            if child.keyword == "taakse":
                command = "moveBackward(" + str(child.child.value) + ")"
                self.command_list.append(command)
            if child.keyword == "oikealle":
                command = "rotate(" + str(child.child.value) + ")"
                self.command_list.append(command)
            if child.keyword == "vasemmalle":
                command = "rotate(" + str(child.child.value*-1) + ")"
                self.command_list.append(command)
            if child.keyword == "tulosta":
                command = 'printToLCD("' + str(child.child.value) + '")'
                self.command_list.append(command)

    def generate_code(self):
        template = open("templates/JavaTemplate.java","r")
        code = open("Main.java","w")
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

        