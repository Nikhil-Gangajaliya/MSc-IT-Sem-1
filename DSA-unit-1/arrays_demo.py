import numpy as np

# Basic arrays
a = np.array([1, 2, 3, 4])
print("Array:", a)

# Range array
b = np.arange(0, 10, 2)
print("Arange:", b)

# Linspace array
c = np.linspace(0, 1, 5)
print("Linspace:", c)

# Logspace array
d = np.logspace(1, 3, 5)
print("Logspace:", d)

# Zeros and Ones
e = np.zeros((2, 3))
f = np.ones((3, 3))
print("Zeros:\n", e)
print("Ones:\n", f)