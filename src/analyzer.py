'''
This module houses the semantic analyzer, which analyzes the tree provided by
the parser for various semantic problems
'''

from src.error_handler import SemanticException
from src.logo_keywords import LOGO_KEYWORDS


class Analyzer:
    '''This class analyzes the tree provided by the parser for various semantic problems'''
    def __init__(self, tree):
        self.tree = tree
        self.keywords = LOGO_KEYWORDS
        self.check_parameters(tree.root)

    def check_parameters(self, root):
        '''
        This method checks the parameter-childen of a node for semantic problems.
        In case it is given a CodeNode as argument, it is run again recursively.
        '''
        for child in root.children:
            if child.token_type() == "code":
                self.check_parameters(child)
            else:
                self.check_parameter_number(child)
                self.check_parameter_type(child)

    def get_parameter_type(self, node):
        '''This method examines the parameter string, and returns its type'''
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
        '''This method checks that a node has the correct amount of children'''
        if node.token_type == "keyword" and node.child is not None:
            SemanticException.keyword_without_child(node.keyword)

    def check_parameter_type(self, node):
        '''This method checks if the parameter of a node is ot the correct type'''
        parameter_type = self.get_parameter_type(node.child)
        correct_type = self.keywords.get(node.keyword)
        if (correct_type == "float" or correct_type == "string") and (node.child.token_type == "bin_operator", parameter_type == "float" or parameter_type == "integer"):
            return
        elif correct_type != parameter_type:
            SemanticException.child_is_invalid_type(self, node.keyword, node.child.value, correct_type, parameter_type)