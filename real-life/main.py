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
print(df.shape)