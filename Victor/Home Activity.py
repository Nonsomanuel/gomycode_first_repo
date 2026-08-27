import pandas as pd
import numpy as np

#Random generation of matrix A
A = np.random.randint(low=2, high=10, size=(4,4))
print('Matrix A')
print (A)

#Random generation of Matrix B
B = np.random.randint(low=2, high=9, size=(4,4))
print('Matrix B')
print(B)

#Adding A&B
C = A+B
print("Addition")
print(C)

#Multiplying A&B
D = A*B
print('Matrix multiplication')
print(D)

#Finding the transpose of both A&B
Transpose = A.T
print('Transpose A')
print(Transpose)

Transpose = B.T
print('Transpose B')
print(Transpose)

#Scalar *5
Scalar = 5*A
print('Scalar product of A')
print(Scalar)

Scalar = 5*B
print('Scalar product of B')
print(Scalar)