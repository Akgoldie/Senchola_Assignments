import pandas as pd

df = pd.read_csv('titanic new.csv')
temp = df
temp['fare'] = temp['fare'].fillna((temp['fare'].mean()))

print(print(temp.isnull().sum()))