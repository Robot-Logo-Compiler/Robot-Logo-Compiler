"""This module is the semantic analyzer"""
from src.error_handler import SemanticException

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
            print(child)
            child.check_type()
            self.check_type(child)

    def check_type(self, node):
        """Compares nodes child's type with wanted type."""

        if hasattr(node, "child"):
            if self.check_type(node.child) not in node.expected_child():
                SemanticException.child_is_invalid_type(node.keyword)
        elif hasattr(node, "child_one"):
            if self.check_type(node.child_one) not in node.expected_child():
                SemanticException.child_is_invalid_type(node.keyword)
        elif hasattr(node, "child_two"):
            if self.check_type(node.child_two) not in node.expected_child():
                SemanticException.child_is_invalid_type(node.keyword)
        return node.token_type()
