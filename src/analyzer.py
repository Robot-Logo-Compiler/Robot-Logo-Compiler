from src.error_handler import InvalidChildTypeException, KeywordWithoutChildException
from src.logo_keywords import LOGO_KEYWORDS


class Analyzer:
    def __init__(self, tree):
        self.tree = tree
        self.KEYWORDS = LOGO_KEYWORDS
        self.check_parameters(tree.root)

    def check_parameters(self, root):
        for child in root.children:
            if child.token_type() == "code":
                self.check_parameters(child)
            else:
                self.check_parameter_number(child)
                self.check_parameter_type(child)

    def get_parameter_type(self, node):
        value = node.value
        try:
            int(value)
            return "integer"
        except ValueError:
            try:
                float(value)
                return "float"
            except ValueError:
                if value[0]=='"':
                    return "string"
                elif value != "":
                    return "Unknown string"
                else:
                    return "Emtpy string"

    def check_parameter_number(self, node):
        if node.token_type == "keyword" and node.child == None:
            raise KeywordWithoutChildException(node.keyword)
            exit()

    def check_parameter_type(self, node):
        parameter_type = self.get_parameter_type(node.child)
        correct_type = self.KEYWORDS.get(node.keyword)
        if (correct_type == "float" or correct_type == "string") and (parameter_type == "float" or parameter_type == "integer"):
            return 
        elif correct_type != parameter_type:
            raise InvalidChildTypeException(node.keyword, node.child.value, correct_type, parameter_type)
            exit()
