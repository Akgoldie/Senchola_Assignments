import pandas as pd

df = pd.read_csv('titanic new.csv')
temp = df
temp['embarked'] = temp['embarked'].fillna("s")

print(print(temp.isnull().sum()))