#from src.error_handler import ParserError
from src.binary_reorganizer import reorder_token_list

class ParserTree:

    def __init__(self, tokens):
        self.root = CodeNode()
        self.create_tree(
            reorder_token_list(tokens)
            )
        #print(reorder_token_list(tokens))
        #print(1)

    def create_tree(self, tokens):
        stack = []
        root = self.root
        for token in tokens:
            while root.complete():
                root = stack.pop()
            #print(len(stack), token)
            if token[0] == "KEYWORD":
                node = KeywordNode(token[1])
            elif token[0] == "PARAMETER":
                node = ParameterNode(value=token[1])
            elif token[0] == "BIN_OP":
                node = BinaryOperationNode(type=token[1])
            root.add_child(node)
            stack.append(root)
            root = node
        if root != self.root:
            pass #ParserError.parameter_without_command(node)

    def type_check(self):
        self.root.return_type()

class CodeNode:

    def __init__(self):
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def token_type(self):
        return "code"

    def complete(self):
        return False

    def return_type(self):
        for child in self.children:
            if child.return_type() is not None:
                pass #ERROR COMES HERE


class KeywordNode:

    def __init__(self, keyword):
        self.child = None
        self.keyword = keyword

    def add_child(self, node):
        self.child = node

    def token_type(self):
        return "keyword"

    def complete(self):
        if self.child is None:
            return False
        return True

    def return_type(self):
        if not self.complete:
            pass #ERROR MISSING PARAMETERS
        elif not self.child.return_type() == "number":
            pass #ParserError.child_is_invalid_type(self.keyword, self.child, "number", self.child.return_type())
        return None

class ParameterNode:

    def __init__(self, value):
        self.value = value

    def token_type(self):
        return "parameter"

    def add_child(self, child):
        pass

    def complete(self):
        return True

    def return_type(self):
        return "number"

class BinaryOperationNode:

    def __init__(self, type):
        self.child1 = None
        self.child2 = None
        self.type = type

    def token_type(self):
        return "bin_operator"

    def add_child(self, child):
        if self.child1 is None:
            self.child1 = child
        elif self.child2 is None:
            self.child2 = child

    def complete(self):
        if self.child2 is None:
            return False
        return True

    def return_type(self):
        if not self.complete:
            pass #ERROR MISSING PARAMETERS
        if self.child1.return_type() == "number":
            pass #ERROR COMES HERE
        if self.child2.return_type() == "number":
            pass #ERROR COMES HERE
        return "number"

#if __name__ == "__main__":
    #tokens = [("KEYWORD", "show"), ("SYMBOL", "left_parn"), ('PARAMETER', '1'),
    # ('BIN_OP', 'plus'), ('PARAMETER', '1'), ("SYMBOL", "right_paren")]
    #tree = ParserTree(tokens)
    #print(tree.root.children[0].child)
