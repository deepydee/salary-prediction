import csv
import random


def years_to_salary(years):
    return years * 200 + 2000 + random.randint(1, 400)

def entry_generator(num_rows):
    i = 0
    while i < num_rows:
        years = random.randint(1, 10)
        yield years, years_to_salary(years)
        i += 1

with open('salaries.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('Years', 'Salary'))
    writer.writerows(entry_generator(100))