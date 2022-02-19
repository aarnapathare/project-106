from statistics import correlation
import pandas as pd
import csv
import plotly.express as px
import numpy as np

df = pd.read_csv("data.csv")
fig = px.scatter(df, x="week", y = "Coffee in ml")
fig.show()

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

week = []
coffee = []

for i in data:
    week.append(float(i[0]))
    coffee.append(float(i[1]))

correlation = np.corrcoef(week, coffee)
print(correlation[0,1])