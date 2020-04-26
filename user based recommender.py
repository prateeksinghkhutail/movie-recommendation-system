
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

dataset=pd.read_csv('ratings.csv')

title_dataset=pd.read_csv('movies.csv')
dataset=pd.merge(dataset,title_dataset,on='movieId')


ratings=pd.DataFrame(dataset.groupby('title')['rating'].mean())
ratings['no_of_ratings']=dataset.groupby('title')['rating'].count()

movie_matrix=pd.pivot_table(dataset,index='userId',columns='title',values='rating')

movie=input("enter the movie you liked:")
movie_user_rating=movie_matrix[movie]

similar_to_movie=movie_matrix.corrwith(movie_user_rating)

corr= pd.DataFrame(similar_to_movie, columns=['correlation'])
corr.dropna(inplace=True)
print("Top similar movies to "+movie+" are:\n")
corr= corr.join(ratings['no_of_ratings'])
corr[corr['no_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(5)