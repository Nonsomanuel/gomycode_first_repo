import pandas as pd
import numpy as np
from math import gamma

df = pd.Series ([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])

Mean = df.mean()
print(df)
print(Mean)

Median = df.median()
print(df)
print(Median)

Mode = df.mode
print(df)
print(Mode)

print(f'Mean: {Mean:,.2f}')
print(f'Median: {Median:,.2f}')


Mode = df.mode()
print(f'Mode: {Mode}')


df = pd.Series ([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
Mean = df.mean()
print(df)
print(f'Mean: {Mean}')

Median = df.mean()

print(f'Median: {Median}')

df = pd.Series ([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
Mean = df.mean()
print(df)
print(f'Mean: {Mean}')

Median = df.median()
print(df)
print(Median)

Mode = df.mode()
print(df)
print(Mode)


print(f'Mean: {Mean:,.2f}')
print(f'Median: {Median:,.2f}')
print(f'Mode: {Mode:}')