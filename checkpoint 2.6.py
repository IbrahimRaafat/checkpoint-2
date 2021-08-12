import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print("array 1:")
print(x)
print("array 2 :")
print(y)
print("Covariance matrix arrays is:",np.cov(x, y))