"""Contains the child-classes and the class ParserTree that the parse function creates
"""
from src.error_handler import SemanticException
from src.logo_functions import LOGO_FUNCTIONS

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

    def __str__(self) -> str:
        return '(CodeNode)->'

class KeywordNode:

    def __init__(self, keyword=None, parameter=None):
        self.child = parameter
        self.keyword = keyword

    def add_child(self, node):
        self.child = node

    def token_type(self):
        return "keyword"

    def check_types(self, st):
        self.child.check_types(st)

    def check_type(self):
        valid_types = ["str","int","float","KeywordNode","Parameternode","BinaryOperationNode","VariableNode","NameVariableNode"]
        if self.child.check_type() not in valid_types:
            SemanticException.child_is_invalid_type(self.keyword)
        return "KeywordNode"

    def __str__(self) -> str:
        return '(' + 'KeywordNode ' + ' keyword: ' + self.keyword.__str__() + ' parameter: ' + self.child.__str__() + ') ->'

class ParameterNode:

    def __init__(self, value=None):
        self.value = value

    def token_type(self):
        return "parameter"

    def check_type(self):
        if self.value.isnumeric():
            return "int"
        elif self.can_be_float(self.value):
            return "float"
        else:
            return "str"

    def check_types(self, st):
        self.get_type()

    def get_type(self):
        if self.can_be_float(self.value):
            return "double"
        if isinstance(self.value, str):
            return "String"
    
    def can_be_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __str__(self) -> str:
        return '(' + 'ParameterNode ' + ' value: ' + self.value.__str__() + ') ->'

class BinaryOperationNode:

    def __init__(self, operand_type="plus", left=None, right=None):
        self.child_one = left
        self.child_two = right
        self.operand_type = operand_type

    def add_child(self, child):
        if self.child_one is None:
            self.child_one = child
        elif self.child_two is None:
            self.child_two = child

    def token_type(self):
        return "bin_operator"
        #Should return number. All binary operators are considered equivalent to numbers

    def check_types(self, st):
        self.child_one.check_types(st)
        self.child_two.check_types(st)

    def check_type(self):
        valid_types = ["int","float","KeywordNode"]
        if self.child_one.check_type() not in valid_types:
            SemanticException.child_is_invalid_type(self)
        if self.child_two.check_type() not in valid_types:
            print("Ff3")
            SemanticException.child_is_invalid_type(self)
        return "float"

    def get_type(self):
        return "double"

    def __str__(self) -> str:
        return '(' + 'BinaryOperationsNode' + ' Child_one: ' + self.child_one.__str__() + ' Child_two: ' + self.child_two.__str__() + ') ->'

class NameVariableNode:
    def __init__(self, name=None):
        self.name = name

    def token_type(self, symbol_table=None):
        if symbol_table is not None:
            return symbol_table[self.name]
        return "variable"

    def check_types(self, st):
        return self.get_type(st)

    def check_type(self):
        if not isinstance(self.name, str):
            SemanticException.child_is_invalid_type('NameVariableNode ')
        return "str"

    def get_type(self, st):
        return "void"

    def __str__(self) -> str:
        return '(' + 'NameVariableNode' + ' Name is: ' + self.name.__str__() + ') ->'

class VariableNode:

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def token_type(self, symbol_table=None):
        if symbol_table is not None:
            return symbol_table[self.name]
        return "variable"

    def check_types(self, st):
        st[self.name.name] = self.value.get_type()

    def check_type(self):
        valid_types_value = ["str","int","float"]
        if self.name.check_type() != "str":
            SemanticException.child_is_invalid_type(self.name)
        if self.value.check_type() not in valid_types_value:
            SemanticException.child_is_invalid_type(self.name)

        return "VariableNode"

    #TestVersion
    def type_check(self, symbol_table):
        if self.name not in symbol_table:
            print("ERROR")
        return symbol_table[self.name]

    def __str__(self) -> str:
        return '(' + 'VariableNode' + ' name: ' + self.name.__str__() + " value: " + self.value.__str__() + ') ->'

class FunctionNode:
    def __init__(self, name=None, parameters=[]):
        self.name = name
        self.parameters = parameters

    def expected_child(self):
        return LOGO_FUNCTIONS[self.name]["parameters"]

    def check_type(self):
        valid_types = ["str","int","float","KeywordNode","Parameternode","Stringnode","BinaryOperationNode","VariableNode","NameVariableNode"]
        for parameter in self.parameters:
            if parameter.check_type() not in valid_types:
                SemanticException.child_is_invalid_type(self.name)

    def check_types(self, st):
        for parameter in self.parameters:
            parameter.get_type(st)

    #testversion
    def type_check(self, symbol_table):
        for i in range(len(self.parameters)):
            if not self.parameters[i].type_check(symbol_table) == LOGO_FUNCTIONS[self.name]["parameters"][i]:
                SemanticException.child_is_invalid_type(self.name)
        return LOGO_FUNCTIONS[self.name]["return"]

    def __str__(self) -> str:
        return '(' + 'FunctionNode' +  ' Name is: ' + self.name + ' Parameters: ' + self.parameters.__str__() + ') ->'
