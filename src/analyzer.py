"""This module is the semantic analyzer"""
from src.error_handler import SemanticException

global symbol_table
symbol_table = {}

class Analyzer:
    """
    This is the analyzer class.
    It goes through the parser tree and checks it for errors with nodes' children and their return type.
    """

    def __init__(self, tree):
        self.go_through_children(tree.root.children)

    def go_through_children(self, tree):
        """Runs the check type function for all children in the parser tree."""

        for child in tree:
            child.create_table(symbol_table)
            child.check_type(symbol_table)
