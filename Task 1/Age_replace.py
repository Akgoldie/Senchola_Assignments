import pandas as pd

df = pd.read_csv('titanic new.csv')
temp = df
temp['age'] = temp['age'].fillna(round(temp['age'].mean()))

print(print(temp.isnull().sum()))