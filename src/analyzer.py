from src.error_handler import SemanticException

class Analyzer:
    def __init__(self, tree):
        self.type_check(tree.root.children)

    def type_check(self, tree):
        for child in tree:
            self.check_type(child)

    def check_type(self, node):
        if hasattr(node, "child"):
            if self.check_type(node.child) not in node.expected_child():
                SemanticException.child_is_invalid_type(node.keyword)
        elif hasattr(node, "child1"):
            if self.check_type(node.child1) not in node.expected_child():
                SemanticException.child_is_invalid_type(node.keyword)
        elif hasattr(node, "child2"):
            if self.check_type(node.child2) not in node.expected_child():
                SemanticException.child_is_invalid_type(node.keyword)
        return node.token_type()
