import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("salaries.csv")

# get all rows with all columns except the last one
x = df.iloc[:,:-1].values

# get all rows with only the last column
y = df.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

model = LinearRegression()
model.fit(x_train, y_train)
a = model.intercept_
b = model.coef_

print(f"y = {a:.2f} + {b[0]:.2f}x")

y_pred = model.predict(x_test)

r2 = r2_score(y_test, y_pred)
print(f"R2 Score: {r2} ({r2:.2%})")

plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color="yellow")
plt.show()