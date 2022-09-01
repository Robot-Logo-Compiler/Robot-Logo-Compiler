from src.logo_parser_tree import KeywordNode, ParserTree, CodeNode, NameVariableNode
from src.logo_parser_tree import ParameterNode, BinaryOperationNode, VariableNode, FunctionNode
from src.error_handler import ParserError
from src.logo_functions import LOGO_FUNCTIONS


class Tokens:
    """A class that manages the token list that was given to the Parser by the Lexer.
        Introduces global variables _tokens and _index
        The list, _token, is traversed through the method consume
    """
    def __init__(self, tokens):
        """ tokens: list of the tokens as tuples
        """
        self._tokens = tokens
        self._index = 0

    def next_token(self):
        """Returns the type of the next token on the list
        """
        if len(self._tokens) >  self._index:
            return self._tokens[self._index][0]
        return "end"

    def next_token_value(self):
        """Returns the value of the next token on the list
        """
        if len(self._tokens) >  self._index:
            return self._tokens[self._index][1]
        return "end"

    def consume(self):
        """Iterates the token list by one
        """
        self._index += 1


def parse(tokens):
    """Driving function that creates a parse tree from an input token list.

    Parsing is based on a recursive descent parser.
    The different levels of recursion are defined as (from higher to lower)
        ParserTree -> CodeBlock -> Statement -> (additive) Expression -> Multiplicative expression -> Parameter

    The different levels of recursion create a subtree and adds it to the main parsing tree.

    Input:rue
        tokens: token list containing tokens as tuples
    Return:
        parserTree-class for the given token list
    """
    tokens = Tokens(tokens)
    root = code_block(tokens)
    tree = ParserTree(root)
    return tree


def expect(expected_token, tokens):
    """Test if next token on the token list is of the expected type, if it's
    not it runs the error function.
    Input:
        tokens: Tokens-class
        token: the expected token value
    Raises:
        ParserError: From src.error_handle module. Results in SystemExit
    """

    if tokens.next_token_value() != expected_token:
        ParserError.missing_right_parenthesis(expected_token, tokens.next_token_value())

def code_block(tokens):
    """
    Creates a CodeBlock object, which is a higher-level abstraction from a statement i.e. may contain
    multiple statements.rue

    For input code that has no loops or any other procedural code calls, a single CodeBlock
    object describes the entire input code.

    The Context-Free Grammar (CFG) rule for the working principle of the CodeBlock is:
        CodeBlock -> Statement CodeBlock | 'Nothing'

    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree representing the CodeBlock
    Raises:
        ParserError: From src.error_handle module. Results in SystemExit
    """
    code = []

    while True:
        if tokens.next_token_value() == "make":
            code.append(variable(tokens))
        elif tokens.next_token() == "KEYWORD":
            code.append(statement(tokens))
        elif tokens.next_token_value() in LOGO_FUNCTIONS:
            code.append(logo_function(tokens))
        elif tokens.next_token() == "end":
            break
        elif tokens.next_token_value() == "right_paren":
            ParserError.found_extra_right_parenthesis()
        elif tokens.next_token_value() == "right_bracket":
            return CodeNode(code)
        else:
            ParserError.expected_keyword_but_found_something_else(tokens.next_token_value())

    return CodeNode(code)


def logo_function(tokens):
    name = tokens.next_token_value()
    tokens.consume()
    parameters = []
    for _ in LOGO_FUNCTIONS[name]["parameters"]:
        parameters.append(additive_expression(tokens))
    return FunctionNode(name, parameters)


def variable(tokens):
    tokens.consume()
    name = parameter(tokens)
    tree = additive_expression(tokens)
    return VariableNode(name, tree)


def statement(tokens):
    """
    Creates a tree representing a statement by producing KeywordNode objects.
    A statement is a single command containing a keyword and its required parameter e.g. Forward Sqrt 2.

    Keyword Expressions differ from Keyword Statements in that keyword expressions contain binary operations.
    E.g. Forward 3 + 3 is an expression while Forward Sqrt 2 is a statement.

    CFG rule for statements is:
        Statement -> Keyword Expression | Keyword Statement

    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree repsresenting the Statement
    """
    keyword = tokens.next_token_value()
    tokens.consume()

    if tokens.next_token() == "KEYWORD":
        current_parameter = statement(tokens)
        return KeywordNode(keyword, current_parameter)

    current_parameter = additive_expression(tokens)
    return KeywordNode(keyword, current_parameter)


def additive_expression(tokens):
    """
    Creates a tree representing an expression containing binary operators.
    By default all expressions are additive_expressions, thus the names are used interchangeably here.
    Multiplicative expressions are handled first in accordance with mathematical order of operations.

    Therefore, the CFG rule for expressions is:
        Expression ->       Multiplicative Expression "+" Expression
                        |   Multiplicative Expression "-" Expressionrue
                        |   Multiplicative Expression
    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree repsresenting the Expression
    """
    tree = multiplicative_expression(tokens)

    while tokens.next_token_value() == "plus" or tokens.next_token_value() == "minus":

        operator = tokens.next_token_value()
        tokens.consume()

        tree_right = multiplicative_expression(tokens)
        tree = BinaryOperationNode(operator, tree, tree_right)

    return tree


def multiplicative_expression(tokens):
    """
    Creates a tree representing a multiplicative expression.
    Please read the docstring of additive_expression for further details

    The CFG rule is:
        Expression ->       Parameter "*" Multilicative Expression
                        |   Parameter "/" Multilicative Expression
                        |   Parameter

    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree repsresenting the Multiplicative Expression
    """
    tree = parameter(tokens)

    while tokens.next_token_value() == "multiply" or tokens.next_token_value() == "divide":

        operator = tokens.next_token_value()
        tokens.consume()

        tree_right = parameter(tokens)
        tree = BinaryOperationNode(operator, tree, tree_right)

    return tree

# pylint: disable=R1710
def parameter(tokens):
    """
    Creates a parameter tree and as its name suggests, handels the return of all parameters.
    The lowest level of recursion in the recurisve descent.

    CFG rule is:
        Parameter -> number | string | Expressions containing parenthesis

    Input:
        tokens: Tokens-class
    Return:
        Root of the tree representing the parameter
    Raises:
        ParserError: From src.error_handle module. Results in SystemExit
    """


    if tokens.next_token() == "PARAMETER":
        
        tree = ParameterNode(tokens.next_token_value())
        tokens.consume()
        return tree

    if tokens.next_token() == "VARIABLE":
        tree = NameVariableNode(tokens.next_token_value())
        tokens.consume()
        return tree

    elif tokens.next_token() == "KEYWORD":
        tree = statement(tokens)
        return tree

    elif tokens.next_token() == "FUNCTION" and tokens.next_token_value() in LOGO_FUNCTIONS:
        tree = logo_function(tokens)
        return tree

    elif tokens.next_token_value() == "minus":
        tokens.consume()
        tree = parameter(tokens)
        return BinaryOperationNode("multiply", tree, ParameterNode(-1))

    elif tokens.next_token_value() == "left_paren":
        tokens.consume()
        tree = additive_expression(tokens)
        # print("PARAMETER TOKEN VALUE", tokens.next_token_value())
        expect("right_paren", tokens)

        tokens.consume()
        return tree

    elif tokens.next_token_value() == "left_bracket":
        tokens.consume()
        tree = code_block(tokens)

        expect("right_bracket", tokens)
        tokens.consume()

        return tree

    else:
        ParserError.expected_parameter_but_found_something_else(tokens.next_token_value())


