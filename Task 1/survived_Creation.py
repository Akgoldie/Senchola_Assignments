import pandas as pd

df = pd.read_csv('titanic new.csv')
temp = df
temp['Alive or Dead'] = ["Alive " if x ==1 else "Dead" for x in temp['survived']]

print(temp)