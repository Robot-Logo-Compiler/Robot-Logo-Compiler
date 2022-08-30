"""This module is the semantic analyzer"""

global symbol_table
symbol_table = {}

class Analyzer:
    """
    This is the analyzer class.
    It goes through the parser tree and checks it for errors with nodes' children and their return type.
    """

    def __init__(self, tree, symbol_table={}):
        print(tree.root)
        self.go_through_children(tree.root, symbol_table)

    def go_through_children(self, tree, symbol_table):
        """Runs the check type function for all children in the parser tree."""
        print("Analyzing start")
        tree.check_type(symbol_table)
        print("print for end")
