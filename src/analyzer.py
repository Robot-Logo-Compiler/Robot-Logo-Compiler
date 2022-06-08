from src.error_handler import SemanticError
from src.logo_keywords import LOGO_KEYWORDS


class Analyzer:
    def __init__(self, tree):
        self.tree = tree
        self.KEYWORDS = LOGO_KEYWORDS
        self.check_parameters(tree.root)

    def check_parameters(self, root):
        for child in root.children:
            if child.token_type() == "code":
                self.check_parameter(child)
            else:
                self.check_parameter_number(child)
                self.check_parameter_type(child)

    def get_parameter_type(self, node):
        value = node.value
        if isinstance(value, int):
            return "integer"
        elif isinstance(value, float):
            return "float"
        elif value[0]=='"':
            return "string"
        else:
            return None

    def check_parameter_number(self, node):
        if node.token_type == "keyword" and node.child == None:
            SemanticError.keyword_without_child(node.keyword)


    def check_parameter_type(self, node):
        parameter_type = self.get_parameter_type(node.child)
        correct_type = self.KEYWORDS.get(node.keyword)
        if correct_type == float and (parameter_type == float or parameter_type == int):
            return
        elif correct_type != parameter_type:
            raise SemanticError("child_is_invalid_type", node.keyword, node.child.value, correct_type, parameter_type)
