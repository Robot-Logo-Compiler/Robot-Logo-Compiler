# Code Generator

## Overview
Code generator generates the final Java code from parser tree using a leJOS-supported Java template.

## The code
The class has a constructor with the parsed tree as parameter named as ```tree``` which consists of Parser Tree classes as nodes built into a tree structure. See Parser Tree documentation for detailed information.

The compiler uses code generator in two phases: First, a command list is created from the parsed tree with a command attached method. Second, this list is written into a template file after a code-insert comment.

## Dependencies
For generating variables (Logo command ```MAKE```), the class imports ```parser_tree.py``` modules VariableNode class to identify variable types.

For a template to insert the ready Java code, the class uses ```JavaTemplate.java``` located in the ```templates``` folder.

## Known issues
At the moment, code generator only supports functions with one parameter.
