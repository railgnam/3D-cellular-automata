# cellular automata experiments


## 1. simple cellular automata 2D

- Wolfram style

This program is a simple program generating complex random patterns.

### rule based program

The next line is generated based on rules,

where the 3 relative digits in the line above (left,top,right)

define the digit in the new line.

Therefore the number_of_rules is 2^3 = 8. Its nice to to use decimal to binary conversion to generate rule code.

### data and representation

The data is stored and the graphics is represented per line in strings of bytes, e.g.,

`new_line = '00101000111101100'`

### pseudo-code

- create a code dictionary
- play the rule using dictonary keys
- prints the string, '1' replaced to '_'

## 2. game of life in 2.5D - layer by layer buildup

> 2D + time shown in 3D
> amount of filled adjacent cells (3x3) in the previous layer define the new cell in the nextlayer

- game of life like cellular automata
- iterating through layers
- iterations are stored in a 3D numpy array
- and shown in a voxel

- amount of filled adjacent cells in the previous layer define the new layer

## 3. game of life in real 3D

> the program iterates through the entire space per step
> cells are defined based on the spatial neighbors (3^3-1)




