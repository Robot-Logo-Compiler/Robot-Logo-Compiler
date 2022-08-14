# Lexer

## Overview
Lexer (also known as lexical analysis) and is the part of compiler where the source code is split into words and then built into a list of tokens for parser. A token is a tuple containing the both the word itself and it's identified purpose.

## The code
Lexer has a constructor with the source code as parameter named as ```input_code``` which is the source code turned into a string object. Lexer doesn't run at initiation for the method ```create_tokens``` needs to be called. When called, lexer first splits ```input_code``` into a list of words with all symbols separated and line changes removed. Then, the lexical analysis is performed. Each word is given a meaning being either a command (found in keywords) or a parameter. With this information (unless an error has occurred), a word is turned into a token and added to token list. Last, the token list is returned.


## Dependencies
```logo_keywords.py``` contains all (key)words lexer can interpret as commands, symbols, setting variables, and math operations and functions. Keywords are supported in English and Finnish. See also [user instructions](https://github.com/Robot-Logo-Compiler/Robot-Logo-Compiler/blob/main/Documentation/instructions.MD) for preset commands.

## Known issues
At the moment, lexer raises error with variable names it should accept. For example, some Scandinavian alphabets such as å,ä and ö should be ok but are not.

Also, Lexer has a symbol table but has no need for one.
