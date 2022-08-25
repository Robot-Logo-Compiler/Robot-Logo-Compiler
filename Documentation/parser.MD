# Parser

Parsing of the tokens created by lexical analysis (by ```lexer.py```) is performed by ```logo_parser.py```.

The current implementation of a parser uses recursive descent to create a parse tree.
The parse tree consists of nodes formed by objects specified by ```logo_parse_tree.py```.
Please see the section called Parse Tree Nodes for further details.

The parser utilizes the ```Tokens``` class to handle all of the functions related to the token list created by ```lexer.py```. Because each token consists of a keyword and its possible associated value, the ```Tokens``` class uses the methods ```next_token``` and ```next_value``` to fetch each of these respectively.

The main driver function for parsing is called ```parse```. The entire parsing process is initiated by the creation of a ```code_block```. This will begin the process of recursive descent during which the entire parse tree is created in a top-down fashion starting from the root node that is of a ```CodeNode``` class type.

## Recursive Descent

The production of further nodes on to the parse tree is propagated by the production rules specified by the rest of the methods in the parser: ```code_block```, ```statement```, ```additive_expression```, ```multiplicative_expression``` and ```parameter```. This method of production is exactly similar to the production rules specified by a Context-Free-Gramamr (CFG). Please familiarize yourself with this concept in order to better understand the rest of this section.

The following descriptions for each of the earlier specified methods can also be found in the docstrings of ```logo_parser.py```.
Each of the methods will propagate the creation of the tree further by creating its own subtree and attaching this subtree as a branch on the main root tree, which is seeded from the root node.

## Production rules for recursive descent

### CodeBlocks / CodeNodes

We are using the term CodeBlocks and CodeNodes interchangeably in technical terms. For clarification, CodeNode is the name of the class that executes the construction of a code block in our implementation.

For input code that has no loops or any other procedural code calls, a single CodeBlock object describes the entire input code.

The Context-Free Grammar (CFG) rule for the working principle of the CodeBlock is:

        CodeBlock -> Statement CodeBlock | 'Nothing'


### Statements

A statement is a single command containing a keyword and its required parameter e.g. Forward Sqrt 2.
Keyword Expressions differ from Keyword Statements in that keyword expressions contain binary operations.
E.g. Forward 3 + 3 is an expression while Forward Sqrt 2 is a statement.

CFG rule for statements is:

    Statement ->        Keyword Expression | Keyword Statement

### Expressions

These can be further classified into additive and multiplicative expressions and create arithmetic expressions in accordance with their names.

### Additive expressions
By default all expressions are additive_expressions, thus the names are used interchangeably here.
Multiplicative expressions are handled first in accordance with mathematical order of operations.

Therefore, the CFG rule for additive expressions is:

    Expression ->       Multiplicative Expression "+" Expression
                    |   Multiplicative Expression "-" Expression
                    |   Multiplicative Expression

### Multiplicative expressions

Please read the section on additive expressions for further details.

The CFG rule for multiplicative expressions is:

    Expression ->       Parameter "*" Multilicative Expression
                    |   Parameter "/" Multilicative Expression
                    |   Parameter

### Parameters

The lowest level of recursion in the recurisve descent meaning that the direction of recursion reverses upwards from downwards. As its name suggests, handels the return of all parameters.

CFG rule is:

    Parameter ->        Number (includes, integers, floats and doubles)
                    |   String
                    |   Expressions containing parenthesis

