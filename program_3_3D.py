__author__ = "Laszlo Mangliar"
__copyright__ = "Copyright 2024, Cellular Automata Experiments"
__license__ = "MIT"

"""
OVERVIEW
cellular automata
voxel version
generates and saves several image results of a list of rules

game of life style cellular automata in 3D
v1: iterative layer buildup
"""

import numpy as np
import math as math
import random as r
import matplotlib.pyplot as plt

def get_first_layer(size, index_u = -1, index_v = -1):
    """create first layer of zeros
    replace one cell to a one"""
    layer = np.zeros((size, size))
    for i in index_u:
        for j in index_v:
            layer[i, j] = 1

    return layer

def get_first_layer_circle(size, center, min_radius, max_radius):
    """create first layer of zeros
    replace one cell to a one"""
    layer = np.zeros((size, size))
    x,y = center
    for i in range(size):
        for j in range(size):
            d = ((i - x) ** 2 + (j - y) ** 2) ** 0.5
            if d < max_radius and d > min_radius:
                layer[i, j] = 1
            
    return layer

def get_first_layer_random(size):
    """create first layer of random zeros or ones
    """
    layer = np.random.randint(0, 2, size = [size, size])
    return layer

def cellular_automata_layer_buildup(first_layer, min = 2, max = 6, layer_count = 10):
    """runs the cellular automata
    game of life rules
    new cell is based on the previous layers adjacent cells

    3D method:
    layer by layer buildup

    creating new layer:
    vstack nine rolled versions of the previous layer
    sum the stack
    apply the rule based on the sum.

    returns image_3D / np.array"""

    
    layer = first_layer
    # s = layer.shape
    s2 = (1, *layer.shape)
    print(s2)
    first_layer.reshape(s2)
    image_3D = [first_layer]

    for i in range(layer_count - 1):
        # sum adjacent cells
        l = np.roll(layer, -1, 0)
        r = np.roll(layer, 1, 0)

        tl = np.roll(l, 1, 1)
        t = np.roll(layer, 1, 1)
        tr = np.roll(r, 1, 1)

        bl = np.roll(l, -1, 1)
        b = np.roll(layer, -1, 1)
        br = np.roll(r, -1, 1)

        nine_adjacent_sum = layer + l + r + tl + t + tr + bl + b + br

        # logical mask
        a = nine_adjacent_sum <= max
        b = nine_adjacent_sum >= min
        lives = np.logical_and(a, b)

        # create new layer [digits array]
        new_layer = np.zeros(layer.shape)
        new_layer[lives] = 1

        # replace old layer with new
        layer = new_layer

        # append new_layer to image (why cant stack?)
        s = new_layer.shape
        new_layer.reshape(s2)
        image_3D.append(new_layer)
    
    cell = np.asarray(image_3D)
    return cell

# attributes
size = 20
layer_count = 20

min = 4
max = 4

random = True
indexs = [2,3,4]

save = True
circle = True
r1 = 2
r2 = 5

note = ''


##################### init
if random:
    first_layer = get_first_layer_random(size)
    txt = 'random'
else:
    first_layer = get_first_layer(size, indexs, indexs)
    txt = str(indexs)[1:-1].replace(', ', '-')
    print(txt)

if circle:
    first_layer = get_first_layer_circle(size, [10,10], r1, r2)
    txt = 'circle-r%s-r%s' %(r1, r2)

####################### run the cellular automata
image_3D = cellular_automata_layer_buildup(first_layer, min, max, layer_count)
image_3D = np.asarray(image_3D, dtype=np.bool_)
image_3D = np.transpose(image_3D)

# ################## visualise
# # and plot everything
fig = plt.figure(figsize = [5, 5], dpi = 200)
ax = fig.add_subplot(projection='3d')
ax.set_proj_type('persp', focal_length = 0.4)

# voxels
ax.voxels(image_3D, facecolors = [0.7] * 3, ) #edgecolors = [0] * 3)

# style
fig.suptitle("CA 2.5D >>  min-%s_max-%s_start-%s" %(min, max, txt), fontsize = 5)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# save
if save:
    plt.savefig('img/CA_2.5D/CA_2.5D_min-%s_max-%s_start-%s-%s.png' %(min, max, txt, note), bbox_inches='tight', dpi = 200)
    print('saved')


plt.show()








