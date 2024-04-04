__author__ = "Laszlo Mangliar"
__copyright__ = "Copyright 2024, Cellular Automata Experiments"
__license__ = "MIT"

"""
OVERVIEW
cellular automata
pixel version
generates and saves several image results of a list of rules

for a cell output in a new layer
the rule reads the previous level adjacent cells (9 cell)
512 rule


data and graphics stored and represented in binary strings in nested lists per layer.
number_of_rules = 2^9
generate rule code and the first layer
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

def get_first_layer(size, index_u = -1, index_v = -1):
    """create first layer of zeros
    replace one cell to a one"""
    layer = []
    for i in range(size):
        string = ''
        for j in range(size):
            string += '0'
        layer.append(string)
    
    index_v = index_v % size
    index_u = index_u % size
        
    # replace character
    layer = layer[:index] + '1' + layer[(index + 1):]
    return layer

def get_first_line_random(size):
    """create first layer of random zeros or ones
    """
    layer = []
    for i in range(size):
        string = ''
        for j in range(size):
            string += str(r.randint(0,1))
        layer.append(string)
    
    index_v = index_v % size
    index_u = index_u % size
    
    return layer

def get_rule_code_3x3(rule):
    rule = rule % 2**9
    """code is length 2^9 binary format of int(rule)"""
    code = '{0:0512b}'.format(int(rule))
    print('\nrule: ', rule, '>>', code)
    return code

def generate_rulebook_3x3(code):
    """creates a rule dictonary
    keys: each of the 512 input cases (9 character, 2^9 cases)
    values: each of the 512 code charachters"""
    # prepare the input_cases for the rule
    input_cases_int = []
    input_cases_str = []
    for i in range(512):
        rule_variation_string = '{0:09b}'.format(i)
        input_cases_str.append(rule_variation_string)
        # input_cases_int.append([int(rule_variation_string[i]) for i in range(3)])

    # rule dictonary
    rule_dict = {}
    for i, input_case in enumerate(input_cases_str):
        rule_dict[input_case] = code[i]
    return rule_dict

def cellular_automata_3D(rule_dict, first_layer, layer_count = 100, print_in_terminal = False, sleep_sec = None):
    """runs the cellular automata
    optionally prints in terminal '0', '_'
    returns the image_3D: nested list of numbers"""
    # create image_3D
    image_3D = [first_layer]
    new_layer = first_layer
    # create layers
    points = []
    for z in range(layer_count):
        old_layer = new_layer
        new_layer = []
        # make rows
        for u in range(len(old_layer)):
            # guideline = old_layer[u]
            # make new line
            # iterate on guideline > outputs new character by the rule
            new_line = ''
            L = len(first_layer[0])
            for i in range(L):
                case1 = old_layer[u-1][i - 1] + old_layer[u-1][i] + old_layer[u-1][(i + 1) % L]
                case2 = old_layer[u][i - 1] + old_layer[u][i] + old_layer[u][(i + 1) % L]
                case3 = old_layer[u+1][i - 1] + old_layer[u+1][i] + old_layer[u+1][(i + 1) % L]
                digit = rule_dict[case1 + case2 + case3]
                if digit == 1:
                    points.append([i,u,z])
                newline += digit
            new_layer.append(new_line)

        image_3D.append(new_layer)
    return image_3D

rules = [
    61, 62, 118, 120, 131, 135,149, 154, 166, 169,
    173, 178, 180, 210, 225
]
rules = [341, 511, 16] # pyramid, black, tower
rules = [16] # tower

for rule in rules:
    # attributes
    size = 100
    # rule = 154
    index = 49
    layer_count = 10



    ##################### init
    first_layer = get_first_layer(size, index)
    # first_line = get_first_layer_random(size)

    # make the rules
    code = get_rule_code_3x3(rule)
    rule_dict =  generate_rulebook_3x3(code)


    ####################### run the cellular automata
    image_3D = cellular_automata_3D(rule_dict, first_layer, layer_count, False)


    ################## visualise
    # # plt.show()







