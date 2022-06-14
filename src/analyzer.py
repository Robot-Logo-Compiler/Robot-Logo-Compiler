'''
This module houses the semantic analyzer, which analyzes the tree provided by
the parser for various semantic problems
'''

from src.error_handler import SemanticException
from src.logo_keywords import LOGO_KEYWORDS, LOGO_KEYWORDS_BINARY_OPERATIONS


class Analyzer:
    '''This class analyzes the tree provided by the parser for various semantic problems'''
    def __init__(self, tree):
        self.tree = tree
        self.keywords = LOGO_KEYWORDS
        self.binary_keywords = LOGO_KEYWORDS_BINARY_OPERATIONS
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
                if value != "":
                    return "Unknown string"
                return "Emtpy string"

    def check_parameter_number(self, node):
        '''This method checks that a node has the correct amount of children'''
        if node.token_type in ["keyword", "bin_operator"] and node.child is None:
            SemanticException.keyword_without_child(self, node.keyword)
        elif node.token_type == "bin_operator" and (not node.child1 or not node.child2):
            SemanticException.wrong_number_of_parameters(self, node.keyword, len(node.children), 2)

    def check_parameter_type(self, node):
        '''This method checks if the parameter of a node is of the correct type'''
        if node.token_type == "keyword":
            if node.child.token_type == "bin_operator":
                self.check_parameters(node.child)
                return
            parameter_type = self.get_parameter_type(node.child)
            correct_type = self.keywords.get(node.keyword)
            if correct_type in ["float", "string"] and parameter_type in ["float", "integer"]:
                return
            if correct_type != parameter_type:
                SemanticException.child_is_invalid_type(self, node.keyword, node.child.value, correct_type, parameter_type)
        elif node.token_type == "bin_operator":
            for child in [node.child1, node.child2]:
                if child.token_type == "bin_operator":
                    self.check_parameters(child)
                    return
                parameter_type == self.get_parameter_type(child)
                if parameter_type not in ["float", "integer"]:
                    SemanticException.child_is_invalid_type(self, node.type, child.value, "numeric", parameter_type)
                    exit()
