import plotly.figure_factory as ff
import statistics
import csv
import random
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv("110-main/data.csv")
data = df["temp"].tolist()

population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("population mean:- ", population_mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

fig = ff.create_distplot([data],["temp"], show_hist = False)
fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0, 1], mode="lines", name="MEAN"))
fig.show()
