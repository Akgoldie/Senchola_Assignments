"""
1.	Infancy (neonate and up to one year age)
2.	Childhood (1 to 11 years old)
3.	Adolescence or teenage (from 12 to 18 years old)
4.	Early adulthood (18 to 30 years)
5.	Middle adulthood (30 to 45 years)
6.	Late adulthood (45 to 60 years)
7.	Early old age (60 to 75 years)
8.	Middle old age (75 to 90 years)
9.	Late old age (over 90 years)
"""

import pandas as pd
import numpy as np

df = pd.read_excel('Final_Data.xlsx')
temp = df

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

values = ["Infancy",
"Childhood","teenage",
"Early adulthood",
"Middle adulthood",
"Late adulthood",
"Early old age",
"Middle old age",
"Late old age"]

temp['Age Types'] = np.select(conditions, values)

print(temp)