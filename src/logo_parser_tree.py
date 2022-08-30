"""Contains the child-classes and the class ParserTree that the parse function creates
"""
from src.error_handler import SemanticException, TypeException
from src.logo_functions import LOGO_FUNCTIONS

class ParserTree:

    def __init__(self, root):
        self.root = root

class CodeNode:

    def __init__(self, children=[]):
        self.children = children

    def check_type(self, symbol_table):
        for child in self.children:
            child.check_type(symbol_table)
        return "codeblock"
    
    def __str__(self) -> str:
        code = ""
        for child in self.children:
            code += child.__str__() + "\n"
        return code

class KeywordNode:

    def __init__(self, keyword=None, parameter=None):
        self.child = parameter
        self.keyword = keyword

    def add_child(self, node):
        self.child = node

    def token_type(self):
        return "keyword"

    def create_table(self, symbol_table):
        self.child.create_table(symbol_table)

    def check_type(self, symbol_table):
        for i in range(len(LOGO_FUNCTIONS[self.keyword]["parameters"])):
            if LOGO_FUNCTIONS[self.keyword]["parameters"][i] == "any":
                self.child.check_type(symbol_table)
            elif not self.child.check_type(symbol_table) in LOGO_FUNCTIONS[self.keyword]["parameters"][i]:
                TypeException.function_got_wrong_parameter_type(
                    self.keyword,
                    self.child.check_type(symbol_table),
                    LOGO_FUNCTIONS[self.keyword]["parameters"][i])
        return LOGO_FUNCTIONS[self.keyword]["return"]

    def __str__(self) -> str:
        return f"{self.keyword} {self.child}"

class ParameterNode:

    def __init__(self, value=None):
        self.value = value

    def token_type(self):
        return "parameter"

    def check_type(self, symbol_table):
        if self.can_be_float(self.value):
            return "number"
        else:
            return "str"

    def get_type(self):
        if self.can_be_float(self.value):
            return "number"
        if isinstance(self.value, str):
            return "str"
    
    def can_be_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __str__(self) -> str:
        return str(self.value)

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

    def create_table(self, symbol_table):
        self.child_one.create_table(symbol_table)
        self.child_two.create_table(symbol_table)

    def check_type(self, symbol_table):
        if self.child_one.check_type(symbol_table) != "number":
            TypeException.binary_operation_something_that_is_not_a_number()
        if self.child_two.check_type(symbol_table) != "number":
            TypeException.binary_operation_something_that_is_not_a_number()
        return "number"

    def get_type(self):
        return "number"

    def __str__(self) -> str:
        return f"{self.child_one} {self.operand_type} {self.child_two}"

class NameVariableNode:
    def __init__(self, name=None):
        self.name = name

    def create_table(self, symbol_table):
        return self.get_type(symbol_table)

    def check_type(self, symbol_table):
        if symbol_table == {}:
            return "str"
        if self.name not in symbol_table:
            print("ERROR")
        return symbol_table[self.name]

    def get_type(self, symbol_table):
        if not isinstance(self.name, str):
            SemanticException.child_is_invalid_type('NameVariableNode ')
        return "str"

    def __str__(self) -> str:
        return f":{self.name}"

class VariableNode:

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def check_type(self, symbol_table):
        if self.name.check_type(symbol_table) != "str":
            TypeException.function_got_wrong_parameter_type("make", self.name.check_type(symbol_table), "string")
        symbol_table[self.name.__str__()] = self.value.check_type(symbol_table)
        return None

    def __str__(self) -> str:
        return f"make {self.name} {self.value}"

class FunctionNode:
    def __init__(self, name=None, parameters=[]):
        self.name = name
        self.parameters = parameters

    def expected_child(self):
        return LOGO_FUNCTIONS[self.name]["parameters"]

    def create_table(self, symbol_table):
        for parameter in self.parameters:
            parameter.get_type(symbol_table)

    def check_type(self, symbol_table):
        for i in range(len(self.parameters)):
            if LOGO_FUNCTIONS[self.name]["parameters"][i] == "any":
                self.parameters[i].check_type(symbol_table)
            elif not self.parameters[i].check_type(symbol_table) == LOGO_FUNCTIONS[self.name]["parameters"][i]:
                TypeException.function_got_wrong_parameter_type(self.name, self.parameters[i].check_type(symbol_table, LOGO_FUNCTIONS[self.name]["parameters"][i]))
        return LOGO_FUNCTIONS[self.name]["return"]

    def __str__(self) -> str:
        string = self.name
        for parameter in self.parameters:
            string += f" {parameter}"
        return string + "\n"
