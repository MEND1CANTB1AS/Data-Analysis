import pandas as pd
import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Overall Runtimes of Movies

df = pd.read_csv("netflix_titles.csv")
df.dataframeName = 'netflix_titles.csv'
nRow, nCol = df.shape
#Filter out the runtime of movies from show seasons
movies = df.loc[df['type'] == 'Movie']
movies.to_csv('movies.csv')
#Formats the duration column to have leading zeros
movies['duration'] = movies['duration'].apply('{:0>7}'.format)

# print(movies)
# print(movies['duration'].value_counts().sort_index(axis=0, ascending=True).apply('{:0>3}'.format))
runtime = movies['duration'].apply('{:0>3}'.format).str.extract('(^\d*)')
runtime.to_csv('runtime.csv')
# print("Total Time of all movies: ", total_time, " minutes")
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(movies['duration'].value_counts().sort_index(axis=0, ascending=True))
movies['duration'].value_counts().sort_index(axis=0, ascending=True).plot(kind='line', figsize=(10, 10))
plt.xlabel("Runtime", labelpad=14)
plt.ylabel("Count", labelpad=14)
plt.title("Movie Runtime", y=1.02)
plt.figure(figsize=(10, 10))


