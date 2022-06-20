"""Contains the child- classes and the class ParcerTree that the parce function creates
"""


class ParserTree:

    def __init__(self, root):
        self.root = root


class CodeNode:

    def __init__(self, children=[]):
        self.children = children

    def add_child(self, node):
        self.children.append(node)

    def token_type(self):
        return "code"

    def complete(self):
        return False


class KeywordNode:

    def __init__(self, keyword=None, parameter=None):
        self.child = parameter
        self.keyword = keyword

    def add_child(self, node):
        self.child = node

    def token_type(self):
        return "keyword"




class ParameterNode:

    def __init__(self, value=None):
        self.value = value

    def token_type(self):
        return "parameter"

    def add_child(self, child):
        pass



class BinaryOperationNode:

    def __init__(self, type="+", left=None, right=None):
        self.child1 = left
        self.child2 = right
        self.type = type

    def add_child(self, child):
        if self.child1 is None:
            self.child1 = child
        elif self.child2 is None:
            self.child2 = child

    def token_type(self):
        return "bin_operator"




