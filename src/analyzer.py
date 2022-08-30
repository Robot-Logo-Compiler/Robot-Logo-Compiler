"""This module is the semantic analyzer"""

class Analyzer:
    """
    This is the analyzer class.
    It goes through the parser tree and checks it for errors with nodes' children and their return type.
    """

    def __init__(self, tree, symbol_table={}):
        self.go_through_children(tree.root, symbol_table)

    def go_through_children(self, tree, symbol_table):
        """Runs the check type function for all children in the parser tree."""
        tree.check_type(symbol_table)
