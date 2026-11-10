import pandas as pd
import numpy as np
from math import gamma

df = pd.Series([15, 18, 19, 20, 20, 20, 21, 23, 23, 24, 24, 25, 45, 30, 33, 37, 21, 38, 42, 49, 50])
Mean = df.mean()
print(df)

print(f'Mean: {Mean:,.2f}')


Median = df.median()
print(f'Median: {Median:,.2f}')

Mode = df.mode()
print(f'Mode: {Mode})')

Variance = df.var(ddof=0)
print(f'Variance: {Variance:,.2f}')

std = df.std()
print(f'Std: {std:,.2f}')