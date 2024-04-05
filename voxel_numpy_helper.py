import numpy as np

size = [5,5,3]
count = np.prod(size)


c = np.indices(size) # z,y,x
z, y, x = c
print(x)
print(y)
print(z)
list_of_coordinates = c.reshape(3, int(count))
print(list_of_coordinates)


val = np.arange(count)
list_of_values = np.vstack((list_of_coordinates, val))

point_list = list_of_values.transpose()
print(point_list)

mask = point_list[:, 3] < 25
print(mask)
filtered = point_list[~mask]
print(filtered)
