import pandas as pd
import numpy as np

df = pd.Series([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
print(df)

Mean = df.mean()
print(Mean)

Median = df.mode()
print(Median)

Mode = df.mode()
print (Mode)

Variance = df.var(ddof=0)
print(Variance)

SD = df.std(ddof=0)
print(SD)

#For the Matrix
A = np.random.randint(1,10,(3,3))
print(f'This is Matrix A: {A}')

B = np.random.randint(1,10,(3,3))
print(f'This is Matrix B: {B}')

#Multiply the matrix
C = A*B
print(f'here is the matrix multiplication:{C}')

#Add the Matrix
D = A+B
print(f'here is the matrix addition:{D}')

#Matrix transpose
Transpose = A.T
print(f'here is the matrix transpose:{Transpose}')

#Scalar multiplication by 5
Scalar_multi = 5 * A
print(f'here is the scalar multiplication:{Scalar_multi}')