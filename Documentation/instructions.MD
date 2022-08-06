## Usage 

The program is run as a command line program. By default files are read from **rootfolder**. The input file containing the input program written in the Logo programming language should be placed in ```root/testfiles```, although the **file path has to still be specified explicitly**. The input file should also contain the extension ```.logo```.

It is important to have the ```JavaTemplate.java``` file in the templates folder before running the program in order to ensure successful compiling. 

The program is run with the terminal command

```Python3 compile.py [name of file and file path if not in rootfolder]```

The compiled Java output file will be in the rootfolder with the name ```Main.java```

## Supported operations

### Moving operations

| Command |                         Function                         |                                  Requirements                                 |
|:-------:|:--------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| Forward |                Displaces the robot forward               |            1 argument as an integer or  a float or a math function.           |
|   Back  |               Displaces the robot backwards              |                                 Same as above                                 |
|   Left  |          Rotates the robot (in degrees) to the left      |                                 Same as above                                 |
|  Right  |              Same as above, but to the right             |                                 Same as above                                 |
|   Show  |              Prints on the robots LCD screen             | At least 1 argument either as an integer, float or string or a math function. |


### Math operations:

| **Name**          | **Keyword/Symbol** | **Function**                                                  |
|-------------------|--------------------|---------------------------------------------------------------|
| Binary operations | + , - , * , /      | Basic Arithmetic                                              |
| Square root       | SQRT               | Math function that outputs the square root of the given input |


### Variable setting

| Command | Function                   | Requirements                                                                                            |
|:-------:|:--------------------------:|:-------------------------------------------------------------------------------------------------------:|
| Make    | Sets a value to a variable | 2 arguments: A string for variable name and a number or string or a functiong returning either of these |



### Order of Operations

The current implementation of the Logo language uses the same order of operations as in the Lisp language.
Nesting functions or operations will always result in the innermost one being executed first.
**Because brackets are optional in this Logo language, the order of operations may not be always intuitive**.
For example SQRT 4 + 4 / 2 would be interpreted as SQRT (4 + 4 / 2) -> SQRT (4 + 2) -> SQRT 6

