import pandas as pd
import numpy as np
url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
df = pd.read_csv(url)
print(df.head(10))
print("===========================")
print(df.columns)
print("============================")
print(df.info()) #data type and missing value
print("============================")
print(df.describe())