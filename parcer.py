
class ParcerTree:

    def __init__(self, tokens):
        self.root = None
        self.create_tree(tokens)
        print(1)

    def create_tree(self, tokens):
        stack = []
        self.root = CodeNode()
        for token in tokens:
            if token[0] == "KEYWORD":
                node = KeywordNode(token[1])
                self.root.add_child(node)
                stack.append(self.root)
                self.root = node
            elif token[0] == "INT":
                node = IntegerNode(value=token[1])
                self.root.add_child(node)
                self.root = stack.pop()


class CodeNode:

    def __init__(self):
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def token_type(self):
        return "code"

class KeywordNode:

    def __init__(self, keyword):
        self.child = None
        self.keyword = keyword

    def add_child(self, node):
        self.child = node

    def token_type(self):
        return "keyword"

class IntegerNode:

    def __init__(self, value):
        self.child = None
        self.value = value

    def token_type(self):
        return "integer"


