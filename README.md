# cellular automata - Wolfram style

## description

This program is a simple program generating complex random patterns.

### rule based program

The next line is generated based on rules,

where the 3 relative digits in the line above (left,top,right)

define the digit in the new line.

Therefore the number_of_rules is 2^3 = 8. Its nice to to use decimal to binary conversion to generate rule code.

### data and representation

The data is stored and the graphics is represented per line in strings of bytes, e.g.,

`new_line = '00101000111101100'`

## pseudo-code

### create a code dictionary

### play the rule using dictonary keys

### prints the string, '1' replaced to '_'
