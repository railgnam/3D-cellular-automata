import numpy as np

size = 2
count = size**3


c = np.indices([size]*3) # z,y,x
# z, y, x = c
# print(x)
# print(y)
# print(z)
list_of_coordinates = c.reshape(3, int(count))
print(list_of_coordinates)


val = np.arange(count)
list_of_values = np.vstack((list_of_coordinates, val))

point_list = list_of_values.transpose()
print(point_list)

mask = point_list[:, 3] < 5
print(mask)
filtered = point_list[~mask]
print(filtered)
