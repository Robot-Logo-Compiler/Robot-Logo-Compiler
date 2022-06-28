from src.logo_parser_tree import KeywordNode, ParserTree, CodeNode, ParameterNode, BinaryOperationNode
from src.error_handler import ParserError

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
    """Function that creates a parse tree from an input token list
    Input:
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
    not it runs the error function
    Input:
        tokens: Tokens-class
        token: the expected token value
    """

    if tokens.next_token_value() != expected_token:
        ParserError.missing_right_parenthesis(expected_token, tokens.next_token_value())

def code_block(tokens):
    """Works on the principle: CodeBlock -> Statement CodeBlock | 'Nothing'
    Creates a tree representing the CodeBlock based on this princible
    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree representing the CodeBlock
    """
    code = []

    while True:
        if tokens.next_token() == "KEYWORD":
            code.append(statement(tokens))
        elif tokens.next_token() == "end":
            break
        elif tokens.next_token_value() == "right_paren":
            ParserError.found_extra_right_parenthesis()
        else:
            ParserError.expected_keyword_but_found_something_else(tokens.next_token_value())

    return CodeNode(code)


def statement(tokens):
    """Works on the principle: Statement -> Keyword Expression | Keyword Statement
    Creates a tree representing the Statement based on this princible
    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree repsresenting the Statement
    """
    keyword = tokens.next_token_value()
    tokens.consume()

    if tokens.next_token() == "KEYWORD":
        parameter = statement(tokens)
        return KeywordNode(keyword, parameter)

    parameter = expression(tokens)
    return KeywordNode(keyword, parameter)


def expression(tokens):
    """Works on the principle: Expression -> TimesExpression "+" Expression
                                           | TimesExpression "-" Expression
                                           | TimesExpression
    Creates a tree representing the Expression based on this princible
    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree repsresenting the Expression
    """
    tree = times_expression(tokens)

    while tokens.next_token_value() == "plus" or tokens.next_token_value() == "minus":

        operator = tokens.next_token_value()
        tokens.consume()

        tree_right = times_expression(tokens)
        tree = BinaryOperationNode(operator, tree, tree_right)

    return tree


def times_expression(tokens):
    """Works on the principle: Expression -> Parameter "*" TimesExpression
                                           | Parameter "/" TimesExpression
                                           | Parameter
    Creates a tree representing the TimesExpression based on this princible
    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree repsresenting the TimesExpression
    """
    tree = parameter(tokens)

    while tokens.next_token_value() == "multiply" or tokens.next_token_value() == "divide":

        operator = tokens.next_token_value()
        tokens.consume()

        tree_right = parameter(tokens)
        tree = BinaryOperationNode(operator, tree, tree_right)

    return tree


def parameter(tokens):
    """Works on the principle: Parameter -> number | string | ( Expression ) | Statement
    Creates a tree representing the Parameter based on this princible
    Input:
        tokens: Tokens-class
    Return:
        Root of the tree representing the parameter
    """
    if tokens.next_token() == "KEYWORD":
        tree = statement(tokens)
        return tree

    elif tokens.next_token() == "PARAMETER":
        tree = ParameterNode(tokens.next_token_value())
        tokens.consume()
        return tree

    elif tokens.next_token_value() == "minus":
        tokens.consume()
        # tree = expression(tokens)
        tree = parameter(tokens)
        # tokens.consume()
        return BinaryOperationNode("multiply", tree, ParameterNode(-1))

    elif tokens.next_token_value() == "left_paren":
        tokens.consume()
        tree = expression(tokens)
        # print("PARAMETER TOKEN VALUE", tokens.next_token_value())
        expect("right_paren", tokens)

        tokens.consume()
        return tree

    else:
        ParserError.expected_parameter_but_found_something_else(tokens.next_token_value())