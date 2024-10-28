import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('salaries-2023.csv')
df = df.dropna()

allowed_languages = ['php', 'js', '.net', 'java']
df = df[df['language'].isin(allowed_languages)]

vilnius_names = ['Vilniuj', 'Vilniua', 'VILNIUJE', 'VILNIUS', 'vilnius', 'Vilniuje']
condition = df['city'].isin(vilnius_names)
df.loc[condition, 'city'] = 'Vilnius'

kaunas_names = ['KAUNAS', 'kaunas', 'Kaune']
condition = df['city'].isin(kaunas_names)
df.loc[condition, 'city'] = 'Kaunas'

allowed_cities = ['Vilnius', 'Kaunas']
df = df[df['city'].isin(allowed_cities)]

df_sorted = df.sort_values(by='salary', ascending=False)
print(df_sorted.head(20))

x = df.iloc[:, -2:-1]
y = df.iloc[:, -1].values
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.scatter(x, y)
plt.show()

df = df[df['salary'] <= 6000]
print(df.shape)

x = df.iloc[:, -2:-1]
y = df.iloc[:,-1].values
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.scatter(x, y)
plt.show()