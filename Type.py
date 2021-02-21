import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.style.use('bmh')
df = pd.read_csv("netflix_titles.csv")
df.dataframeName = 'netflix_titles.csv'
nRow, nCol = df.shape
print(f'There are {nRow} rows and {nCol} columns')

# How many movies and TV shows are on the Netflix Platorm?

media = df['type'].value_counts()
media_list = media.tolist()
print(media_list)

df['type'].value_counts().plot(kind='bar')
plt.xlabel("Type", labelpad=14)
plt.ylabel("Count", labelpad=14)
plt.title("Count of Movies and Shows", y=1.02)
