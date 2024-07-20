import numpy as np

# convert a list to an array.
l = [1, 2, 3, 4, 5]
x = np.array(l)
print(x.ndim)

# slicing with numpy.
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1[::2])

# extracting value from  a 2D array:
np2 = np.array([
    [1, 2, 3, 4, 5],  # ----> this is the 0th row.
    [6, 7, 8, 9, 10]  # -----> this is the 1st row.
])
print(np2[1, 2])  # the 1st value(1) is for which row and the 2nd value is for which element from that row.

# slicing the 2d array
print(np2[0:1,
      1:5])  # here the 1st parameter(0:1) is for the 2 row that exists here and the second one is for slicing the
# selected one.

# dimension of an array.
arr2 = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
y = np.array(arr2)
print(y.ndim)

# defining dimension before and the print it.
arrn = np.array([1, 2, 3, 4, 5], ndmin=10)
print(arrn.ndim)
print(arrn)

# numpy universal functions like

npfunc = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.sqrt(npfunc))
print(np.sum(npfunc))
print(np.log(npfunc))

# shape and reshape in numpy
# creating 1d array
np1_shape = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(np1_shape.shape)

# creating  2d array
np2_shape = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(np2_shape.shape)

# reshaping the 1d array into 2d array
np1_reshape = np1_shape.reshape(3, 4)
print(np1_reshape)

# resahpe into 3d array
np3 = np1_shape.reshape(2, 3, 2)
print(np3)

# back to 1d array from 3d array

np4 = np3.reshape(-1)
print(np4)

# iterate through the arrays
# 1-D array
iteratable_array = np.array([1, 2, 3, 4, 5, 6, 7, 9])
for i in iteratable_array:
    print(i)

print("stop")

# 2-D Array
iteratable_array2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
for j in iteratable_array2d:
    for k in j:
        print(k)
print("stop")

# 3-Array
iteratable_array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(iteratable_array3d):
    # np.nditer loops through array dimensional array simply
    print(x)

# sorting in numpy array
np_sort = np.array([5, 8, 1, 3, 9, 4, 6, 7])
print(np.sort(np_sort))

np_sort2d = np.array([[5, 8, 3, 6], [60, 45, 85, 46]])
print(np.sort(np_sort2d))

np_boolean = np.array([True, False, False, True, False])
print(np.sort(np_boolean))
# o/p ---> [False False False  True  True] as false = 0 & true =1


# numpy searching
np_search = np.array([1,2,3,4,5,6,7,8,9,10])
d = np.where(np_search==2)
print(d)
# where method on array always returns an index and data type of the element
np_search2 = np.array([1,2,34,5,6,7,9,10])
e = np.where(np_search2 % 2 == 0)
print(e)
#here e[0] means that it returns the 1st part means index part.
print(e[0])


# Filtering numpy arrays.
filtered = np1 % 2 == 0
print(filtered)

filtered2 = np1 > 5
# this will filter the array and also access the value of the arrays
print(np1[filtered2])
