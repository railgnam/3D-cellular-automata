import numpy as np

# create an array with indicies
def point_array_with_values(x,y,z):
    pts = np.indices([x,y,z]) # z,y,x
    # z, y, x = c
    # print(x)
    # print(y)
    # print(z)
    count = np.prod([x,y,z])
    pts.reshape(3, int(count))
    # print(list_of_coordinates)

    # add some random values
    val = np.arange(count)
    list_of_values = np.vstack((pts, val))

    # shape as points in rows.
    point_list = list_of_values.transpose()
    print(point_list)

    # filter based on the values
    mask = point_list[:, 3] < 25
    print(mask)
    filtered = point_list[~mask]
    print(filtered)

a = np.arange(10).reshape([1,2,5])
b = np.roll(a, 1, [0,1])
c = np.roll(a, -2, [0,1])
print(b)

cell = np.vstack([a,b,c])
print(cell)