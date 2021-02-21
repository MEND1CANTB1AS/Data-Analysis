import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Here is all the data in a chart

df = pd.read_csv("netflix_titles.csv")
df.dataframeName = 'netflix_titles.csv'
nRow, nCol = df.shape

runtime = pd.read_csv("netflix_titles.csv", usecols=['duration'])

print(runtime)