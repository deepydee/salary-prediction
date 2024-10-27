import csv
import random


with open('salaries-s.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('years', 'salary'))
    i = 0
    while i < 1000:  # generating 1000 rows
        years = random.randint(1, 10)
        salary = years * 200 + 2000 + random.randint(1, 400)
        writer.writerow((years, salary))
        i += 1