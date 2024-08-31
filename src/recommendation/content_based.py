import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

from src.data_processing.load_data import load_data

movies, _r = load_data(source='processed')

tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(movies['combined_text'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def get_content_recommendations(title, cosine_sim=cosine_sim, df=movies, top_n=10):
    # Get the index of the movie that matches the title
    idx = df[df['title'].str.lower() == title.lower()].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top n most similar movies
    sim_scores = sim_scores[1:top_n + 1]  # Exclude the first one because it's the movie itself

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top n most similar movies
    return df['title'].iloc[movie_indices]