import numpy as np
import pandas as pd
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings('ignore')
df = pd.read_csv('movie_dataset.csv')   
features = ['keywords','cast','genres','director']
def combine_features(row):
 return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']


for feature in features:
    df[feature] = df[feature].fillna('')
    
for feature in features:
    df['combined_features'] = df.apply(combine_features,axis=1)
    
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]['title'].values[0]
def get_index_from_title(title):
    return df[df.title == title]['index'].values[0]


movie_user_likes =input("enter the movie you liked")
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
i=0
print("Top 5 similar movies to "+movie_user_likes+" are:\n")
for element in sorted_similar_movies:
    print(get_title_from_index(element[0]))
    i=i+1
    if i>5:
        break