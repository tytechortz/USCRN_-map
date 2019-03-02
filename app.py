import pandas as pd

df = pd.read_csv('./all_uscrn__data.txt', delim_whitespace=True, header=None)

print(df.head())