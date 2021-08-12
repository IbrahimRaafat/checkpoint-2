import numpy as np

my_array = []
a = int(input("Size of array:"))
for i in range(a):
    my_array.append(float(input("Element:")))
my_array = np.array(my_array)
print("numpy array:",my_array)

my_array.tolist()
print("Python list:")
print(my_array)