__author__ = "Laszlo Mangliar"
__copyright__ = "Copyright 2024, Cellular Automata Experiments"
__license__ = "MIT"

"""
OVERVIEW
cellular automata
pixel version
generates and saves several image results of a list of rules


data and graphics stored and represented in binary number strings
number_of_rules = 2^3
generate rule code and the first line
create a code dictionary
play the rule using dictonary keys

convert strings to int
numpy array of zeros and ones
save plt.image
show
"""

import numpy as np
import math as math
import time
import random as r
import matplotlib.pyplot as plt

def get_first_line(length, index = -1):
    """create first line of zeros"""
    hash = ''
    index = index % length
    for i in range(length):
        hash += '0'

    # replace character
    hash = hash[:index] + '1' + hash[(index + 1):]
    return hash

def get_first_line_random(length):
    # first line random
    c2 = ''
    for i in range(length):
        c2 += str(r.randint(0,1))
    return c2

def get_rule_code(rule):
    """code is 8 length binary format of int(rule)"""
    code = '{0:08b}'.format(int(rule))
    print('\nrule: ', rule, '>>', code)
    return code

def generate_rulebook(code):
    """creates a rule dictonary
    keys: each of the 8 input cases
    values: each of the 8 code charachters"""
    # prepare the input_cases for the rule
    input_cases_int = []
    input_cases_str = []
    for i in range(8):
        rule_variation_string = '{0:03b}'.format(i)
        input_cases_str.append(rule_variation_string)
        # input_cases_int.append([int(rule_variation_string[i]) for i in range(3)])

    # rule dictonary
    rule_dict = {}
    for i, input_case in enumerate(input_cases_str):
        rule_dict[input_case] = code[i]
    
    return rule_dict

def cellular_automata(rule_dict, guideline, rows = 100, print_in_terminal = False, sleep_sec = None):
    """runs the cellular automata
    optionally prints in terminal '0', '_'
    returns the image: nested list of numbers"""
    # save first line as numbers
    image = []
    line = [int(i) for i in guideline]
    image.append(line)

    # print line in terminal
    if print_in_terminal:
        # print special characters
        draw = guideline.replace('1', '_')
        print(draw)

    # make rows
    for i in range(rows):
        # make new line
        # iterate on guideline > outputs new character by the rule
        newline = ''
        L = len(guideline)
        for i in range(L):
            case = guideline[i - 1] + guideline[i] + guideline[(i + 1) % L]
            newline += rule_dict[case]

        # save line as numbers
        line = [int(i) for i in newline]
        image.append(line)

        # print line in terminal
        if print_in_terminal:
            # print special characters
            draw = guideline.replace('1', '_')
            print(draw)
            
        # reinit
        guideline = newline
        newline = ''

        # sleep
        if sleep_sec != None:
            time.sleep(sleep_sec)
    
    return image

rules = [
    61, 62, 118, 120, 131, 135,149, 154, 166, 169,
    173, 178, 180, 210, 225
]
for rule in rules:
    # attributes
    width = 400
    rows = 600
    # rule = 154
    index = 200

    print_in_terminal = False


    ##################### init
    # first_line = get_first_line(width, index)
    first_line = get_first_line_random(width)

    # make the rules
    code = get_rule_code(rule)
    rule_dict =  generate_rulebook(code)


    ####################### run the cellular automata
    image = cellular_automata(rule_dict, first_line, rows, False)


    ################## visualise
    image = np.array(image)
    my_dpi = 100
    w = width
    h = rows
    fig, ax = plt.subplots(figsize=(w/10, h/10), dpi=my_dpi)
    im = ax.imshow(image, cmap = plt.cm.gray) #interpolation='bilinear')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(0,-1, "cellular automata 20240403. rule = %s >> %s" %(rule, code), ha='left', va='bottom', fontsize=8, color='black')


    plt.savefig('img/400x600_random/%s_%sx%s_random.png' %(rule,w,h), bbox_inches='tight', dpi = my_dpi)
    print('saved')

    # plt.show()







