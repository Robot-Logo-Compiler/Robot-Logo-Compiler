### Usage 

The current scope of the compiler consists of a main program called ```compile.py``` and several auxiliary programs that are imported to ```compile.py```. These auxiliary programs are the individual subcomponents of a compiler named in accordance with the tasks that they perform (lexer, parser and code generator). 

The program is run as a command line program. By default files are read from **rootfolder**. The input file containing the input program written in the Logo programming language should be placed in ```root/testfiles```, although the **file path has to be specified explicitly**. The input file should also contain the extension ```.logo```.

It is important to have the ```JavaTemplate.java``` file in the templates folder before running the program in order to ensure successful compiling. 

The program is run with the terminal command

```Python3 compile.py [name of file and file path if not in rootfolder]```

The compiled Java output file will be in the rootfolder with the name ```Main.java```

Current scope of the logo programming language: 

|   Command  | Requirements                                                        |
|:----------:|---------------------------------------------------------------------|
| Eteen      | Requires 1 argument as an integer or a float.                       |
| Taakse     | Requires 1 argument as an integer or a float.                       |
| Vasemmalle | Requires 1 argument as an integer or a float.                       |
| Oikealle   | Requires 1 argument as an integer or a float.                       |
| Tulosta    | Requires at least 1 argument either as an integer, float or string. |
