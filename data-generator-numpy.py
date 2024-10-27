import csv
import numpy as np

years = np.random.randint(1, 10 + 1, 1000)
salaries = 2000 + years * 200 + np.random.randint(1, 400 + 1, 1000)

with open('salaries-np.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('years', 'salary'))
    writer.writerows(zip(years, salaries))