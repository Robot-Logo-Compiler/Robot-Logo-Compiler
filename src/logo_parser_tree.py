"""Contains the child-classes and the class ParserTree that the parse function creates
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

    '''KeywordNode only accepts a parameter or a binary operation as a child'''
    def expected_child(self):
        return ["bin_operator", "parameter"]


class ParameterNode:

    def __init__(self, value=None):
        self.value = value

    def token_type(self):
        return "parameter"

    def add_child(self, child):
        pass

    ''' ParameterNode can not have a child, always false'''
    def expected_child(self):
        return []



class BinaryOperationNode:

    def __init__(self, operand_type="+", left=None, right=None):
        self.child1 = left
        self.child2 = right
        self.operand_type = operand_type

    def add_child(self, child):
        if self.child1 is None:
            self.child1 = child
        elif self.child2 is None:
            self.child2 = child

    def token_type(self):
        return "bin_operator"
        #Should return number. All binary operators are considered equivalent to numbers

    ''' binary operation must have a parameter or another binary operation as a child'''
    def expected_child(self):
        return ["bin_operator", "parameter"]

class VariableNode:

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def token_type(self, symbol_table=None):
        if symbol_table is not None:
            return symbol_table[self.name]
        return "variable"

    def expected_child(self):
        return ["string", "parameter"]

class TrueVariableNode:
    def __init__(self, name=None):
        self.name = name

    def token_type(self, symbol_table=None):
        if symbol_table is not None:
            return symbol_table[self.name]
        return "variable"

    def expected_child(self):
        return []
