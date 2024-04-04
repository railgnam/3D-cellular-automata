"""
first draft
generates output in terminal
"""
import time

# settings
ROWS = 100
RULE = 109
WIDTH = 100


# CREATE A CODE DICTONARY
# make a rule
# 8 output digit
code = '{0:08b}'.format(RULE)
print('\nRULE: ', RULE, '>>', code)

# prepare the 8 input_cases for the rule
input_cases_str = []
for i in range(8):
    rule_variation_string = '{0:03b}'.format(i)
    input_cases_str.append(rule_variation_string)

# code dictionary of the rule
rule_dict = {}
for i, input_case in enumerate(input_cases_str):
    rule_dict[input_case] = code[i]


# FIRST LINE
# set up first_line using binary formating
first_line = '{0:0100b}'.format(int(1)) 
draw = first_line.replace('1', '_')
print(draw)


# PLAY THE RULE
guideline = first_line
newline = ''

for i in range(ROWS):
    time.sleep(0.01) # animation effect
    L = len(guideline)
    for i in range(L):
        # match rule dictonary key with the digits above
        case = guideline[i - 1] + guideline[i] + guideline[(i + 1) % L]
        newline += rule_dict[case]
    
    guideline = newline
    newline = ''

    # PRINT THE STRING
    draw = guideline.replace('1', '_')
    print(draw)
    



