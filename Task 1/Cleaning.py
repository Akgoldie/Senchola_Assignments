import pandas as pd
import numpy as np

df = pd.read_csv('titanic new.csv')
temp = df

temp['fare'] = temp['fare'].fillna((temp['fare'].mean()))

temp['embarked'] = temp['embarked'].fillna("s")

temp['age'] = temp['age'].fillna(round(temp['age'].mean()))

temp['Alive or Dead'] = ["Alive " if x ==1 else "Dead" for x in temp['survived']]

conditions = [
    (temp['age'] <= 1),
    (temp['age'] > 1) & (temp['age'] <= 11),
    (temp['age'] > 11) & (temp['age'] <= 18),
    (temp['age'] > 18) & (temp['age'] <= 30),
    (temp['age'] > 30) & (temp['age'] <= 45),
    (temp['age'] > 45) & (temp['age'] <= 60),
    (temp['age'] > 60) & (temp['age'] <= 75),
    (temp['age'] > 75) & (temp['age'] <= 90),
    (df['age'] > 90)
    ]

values = ["Infancy","Childhood","teenage","Early adulthood","Middle adulthood","Late adulthood","Early old age","Middle old age","Late old age"]

temp['Age Types'] = np.select(conditions, values)

df.to_excel("Final_Data.xlsx",index=False)
