# Java Template

## Overview
A Java main class that supports leJOS NXT robots. It doesn't compile unless a special leJOS compiler is installed. See [user instructions](https://github.com/Robot-Logo-Compiler/Robot-Logo-Compiler/blob/main/Documentation/instructions.MD) for further infromation.

## The code
The class has a few special static methods for moving the robot and showing text on its LCD. It is also configurable concerning rotating angles and speed calibration. It is pre-configured for a wheel diameter of 2.165 and track width of 8.46 inches.

## Dependencies
The class uses leJOS NXT and DifferentialPilot libraries for controlling the robot. Morre common FileInputStream and Properties libraries are needed for config file handling.

## Known issues
No issues known.
