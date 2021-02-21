import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Here is all the data in a chart

df = pd.read_csv("netflix_titles.csv")
df.dataframeName = 'netflix_titles.csv'
nRow, nCol = df.shape
print(f'There are {nRow} rows and {nCol} columns')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)