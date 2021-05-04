import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IMDB-Movie-Data.csv')

# Фильмы, относящиеся к нескольким жанрам, более популярны
# Присутствие среди исполнителей определённых актёров повышает рейтинг фильма
# 1) Чем больше доход от фильма, тем выше его рейтинг (False)
# 2) С каждым годом выходит всё больше фильмов (True)
# 3) Самый популярный жанр - Comedy (False)

df['Revenue (Millions)'].fillna(-1, inplace = True)
df['Metascore'].fillna(-1, inplace = True)

a = df.plot(x='Revenue (Millions)', y='Rating', kind='scatter')
plt.show()
b = df['Year'].value_counts().plot(kind = 'barh')
plt.show()
c = df['Genre'].value_counts().plot(kind = 'pie')
plt.show()
print(df.groupby(by='Rating')['Revenue (Millions)'].max())
print(df.groupby(by='Actors')['Rating'].max())
#df.plot(x='Genre', y='Votes', kind='barh')
# Дополнительную информацию о синтаксисе можно найти здесь: https://pandas.pydata.org/docs/

#    82.9
#    58.9

#print(df.groupby(by = 'Votes')['Genre'].agg('max'))
#print(df.groupby(by = 'Actors')['Rating'].agg('max'))
#temp = df.pivot_table(columns = 'Revenue (Millions)',
#               index = 'Title',
#               values = 'Rating',
#               aggfunc = 'max')
#print(temp)
#print(df.groupby(by = 'Revenue (Millions)')['Rating'].agg('max'))

#print(df.describe())