from src.error_handler import ParserError
class ParserTree:

    def __init__(self, tokens):
        self.root = None
        self.create_tree(tokens)
        #print(1)

    def create_tree(self, tokens):
        stack = []
        self.root = CodeNode()
        for token in tokens:
            if token[0] == "KEYWORD":
                node = KeywordNode(token[1])
                self.root.add_child(node)
                stack.append(self.root)
                self.root = node
            elif token[0] == "PARAMETER":
                node = ParameterNode(value=token[1])
                self.root.add_child(node)
                try:
                    self.root = stack.pop()
                except IndexError():
                    ParserError.parameter_without_command(node)
                    exit()
        self.type_check()
    def type_check(self):
        self.root.return_type()


class CodeNode:

    def __init__(self):
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def token_type(self):
        return "code"

    def return_type(self):
        for child in self.children:
            child.return_type()


class KeywordNode:

    def __init__(self, keyword):
        self.child = None
        self.keyword = keyword

    def add_child(self, node):
        self.child = node

    def token_type(self):
        return "keyword"

    def return_type(self):
        if not self.child.return_type() == "number":
            ParserError.child_is_invalid_type(self.keyword, self.child, "number", self.child.return_type())
        return None

class ParameterNode:

    def __init__(self, value):
        self.child = None
        self.value = value

    def token_type(self):
        return "parameter"

    def return_type(self):
        return "number"
