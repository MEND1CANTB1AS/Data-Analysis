import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# headers = ['name', 'date', 'close']
plt.style.use('bmh')
df = pd.read_csv("netflix_titles.csv")
df.dataframeName = 'netflix_titles.csv'
nRow, nCol = df.shape
print(f'There are {nRow} rows and {nCol} columns')

# print(df.dtypes)

media = df['type'].value_counts()
media_list = media.tolist()
print(media_list)
print(df['rating'].value_counts())
df['rating'].value_counts().plot(kind='bar')
plt.xlabel("Rating", labelpad=14)
plt.ylabel("Count", labelpad=14)
plt.title("Count of Movies/Shows by Rating", y=1.02)


