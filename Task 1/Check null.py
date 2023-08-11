import pandas as pd

df = pd.read_csv('titanic new.csv')

print(df.isnull().sum())