from src.logo_parser_tree import KeywordNode, ParserTree, CodeNode, ParameterNode, BinaryOperationNode


class Tokens:
    """A class that manages the token list, providing semi-global variables
    for the parsing funtions
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
        return None
   
    def consume(self):
        """Iterates the token list by one
        """
        self._index += 1


def parse(tokens):
    """Function that creates a parse tree for an input token list
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
        tokens.consume()
        error()


def error():
    """Gives an error message when called
    """
    print("Error has occurred")


def code_block(tokens):
    """Works on the principle: CodeBlock -> Statement CodeBlock | 'Nothing' 
    Creates a tree representing the CodeBlock based on this princible
    Input:
        tokens: Tokens-class
    Returns:
        Root of the tree repsresenting the CodeBlock
    """
    code = []

    while tokens.next_token() == "KEYWORD":
        code.append(statement(tokens))

    return CodeNode(code)


def statement(tokens):
    """Works on the principle: Statement -> Keyword Parameter | Keyword Statement
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
    """Works on the principle: Parameter -> number | string | ( Expression )
    Creates a tree representing the Parameter based on this princible
    Input:
        tokens: Tokens-class
    Return:
        Root of the tree representing the parameter
    """
    if tokens.next_token() == "PARAMETER":
        tree = ParameterNode(tokens.next_token_value())
        tokens.consume()
        return tree

    elif tokens.next_token_value() == "left_paren":
        tokens.consume()
        tree = expression(tokens)
        expect("right_paren", tokens)
        tokens.consume()
        return tree

    else:
        error() #Requires a true Error message

