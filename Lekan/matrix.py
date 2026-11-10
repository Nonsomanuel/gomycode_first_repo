import pandas as pd
import numpy as np
from numpy.ma.core import transpose

A = np.random.randint(low=1, high=10, size=(3, 3))
print("Matrix A:")
print(A)

B = np.random.randint(low=1, high=10, size=(3, 3))
print("Matrix B:")
print(B)
sum = np.add(A, B)
print("Matrix sum:")
print(sum)


product = np.multiply(A, B)
print("Matrix product:")
print(product)

transpose = np.transpose(A)
print("Matrix transpose:")
print(transpose)

transpose = np.transpose(B)
print("Matrix transpose:")
print(transpose)

scalar = 5* A
print("Matrix scalar A :")
print(scalar)

scalar = 5* B
print("Matrix scalar B :")
print(scalar)

