# cellular automata experiments

Cellular Automatas are simple programs generating complex random patterns.

## 1. simple cellular automata 2D

- The next line is generated based on rules,
- where the 3 relative digits in the line above (left,top,right)

- define the digit in the new line.

> Therefore the number_of_rules is 2^3 = 8. Its nice to to use decimal to binary conversion to generate rule code.
> The data is stored and visualised per line in strings of bytes, e.g., `new_line = '00101000111101100'`

## 2. game of life in 2.5D - layer by layer buildup

> 2D + Time = 3D:
- game of life like cellular automata
- amount of filled adjacent cells in the previous layer define the new layer
- iterations are merged into a 3D array
- visualised with voxels

## 3. game of life in real 3D

> 3D + Time = 4D
- the program iterates through the entire space per step
- cells are defined based on the spatial neighbors (3^3-1)
- visualised with animated voxels




