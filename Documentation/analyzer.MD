# Analyzer

## Overview
The analyzer class (also known as semantic analysis) is responsible for comparing variables' types and functions' return values with expected ones using a special symbol table.

## The code
The class has a constructor with the parsed tree as parameter named as tree which consists of Parser Tree classes as nodes built into a tree structure. See Parser Tree documentation for detailed information.

The class runs at initiation and goes recursively through all the tree's nodes and simultaneously building a symbol table for variables and return values.

## Dependencies
```SemanticError``` is a class in ```error_handler.py``` module. If an error has occured while executing semantical analysis,program makes a system exit and a simple Finnish error message is shown.

## Known issues
The program has so many issues right now that it just waits for a rebuild.
