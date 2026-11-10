import pandas as pd
import numpy as np

df =pd.Series([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
print(df)
#find the mean of the data
Mean =df.mean()
print(f'mean: {Mean:,.2f}')

Median =df.median()
print(f'median: {Median:,.2f}')

Mode =df.mode()
print(f'mode: {Mode}')

Variance =df.var(ddof=0)
print(f'variance: {Variance:,.2f}')

std=df.std()
print(f'standard deviation: {std:,.2f}')

#generate random matrix A and b
#add matrix a and b
#multiply matrix a and b
#tranpose of a and b
#scalar multiplication by 5
A = np.random.randint(low=1, high=10, size=(2,3))
print('matrix A:')
print(A)

B = np.random.randint(low=1, high=10, size=(2,3))
print('matrix B:')
print(B)

#Addition
Sum = A + B
print(f'sum of Matrix A and Matrix B:')
print(Sum)

#product
Product = A * B
print(f'Product of Matrix A and Matrix B:')
print(Product)

Transpose = A.T
print(f'Transpose of Matrix A')
print(Transpose)

Transpose = B.T
print(f'Transpose of Matrix B')
print(Transpose)

ScalarMultiplication = 5 * A
print(f'Scalar Multiplication of Matrix A and a product of 5')
print(ScalarMultiplication)

ScalarMultiplication = 5 * B
print(f'Scalar Multiplication of Matrix B and a product of 5')
print(ScalarMultiplication)