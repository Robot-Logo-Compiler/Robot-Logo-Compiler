'''This module goes through the parser tree looking for errors'''
from src.error_handler import InvalidChildTypeException, KeywordWithoutChildException
from src.logo_keywords import LOGO_KEYWORDS


class Analyzer:
    '''This class analyzes the parser tree'''

    def __init__(self, tree):
        self.tree = tree
        self.keywords = LOGO_KEYWORDS
        self.check_parameters(tree.root)

    #def excepthook(type, value, traceback):
        #print(value)
        #sys.excepthook = excepthook

    def check_parameters(self, root):
        '''This function goes through all parser tree nodes and checks their parameters'''

        for child in root.children:
            if child.token_type() == "code":
                self.check_parameters(child)
            else:
                self.check_parameter_number(child)
                self.check_parameter_type(child)

    def get_parameter_type(self, node):
        '''This function returns the given nodes parameter type'''

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
                if value != "":
                    return "Unknown string"
                return "Emtpy string"

    def check_parameter_number(self, node):
        '''This function checks that keyword nodes have children'''

        if node.token_type == "keyword" and node.child is None:
            raise KeywordWithoutChildException(node.keyword)

    def check_parameter_type(self, node):
        '''This function checks that node has correct parameters'''

        parameter_type = self.get_parameter_type(node.child)
        correct_type = self.keywords.get(node.keyword)
        if correct_type in ("float", "string") and parameter_type in ('float', 'integer'):
            return
        if correct_type != parameter_type:
            raise InvalidChildTypeException(node.keyword, node.child.value, correct_type, parameter_type)
            #exit()
