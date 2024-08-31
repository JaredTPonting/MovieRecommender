from src.data_processing.load_data import load_data
from sklearn.preprocessing import StandardScaler, MultiLabelBinarizer
import ast
import pandas as pd
import numpy as np


def main():
    movies, _r = load_data()
    movies['release_year'] = pd.to_datetime(movies['release_date'], errors='coerce').dt.year
    movies['genres'] = movies['genres'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
    movies['genres'] = movies['genres'].apply(lambda x: [i['name'] for i in x])
    # One-hot encode the genres using MultiLabelBinarizer
    mlb = MultiLabelBinarizer()
    genres_dummies = pd.DataFrame(mlb.fit_transform(movies['genres']), columns=mlb.classes_, index=movies.index)
    # Append the one-hot encoded genres to the movies DataFrame
    movies = pd.concat([movies, genres_dummies], axis=1)

    movies['popularity_metric'] = (movies['vote_average'] * movies['vote_count']) / (movies['vote_count'] + 100)

    # Normalize the popularity metric
    scaler = StandardScaler()
    movies['popularity_metric'] = scaler.fit_transform(movies[['popularity_metric']])

    movies[['budget', 'revenue']] = scaler.fit_transform(movies[['budget', 'revenue']])

    # Combine text features into a single field
    movies['combined_text'] = movies['title'].fillna('') + ' ' + movies['overview'].fillna('') + ' ' + movies[
        'tagline'].fillna('')

    movies.to_csv('../../data/processed/movies_metadata.csv', index=False)


if __name__ == '__main__':
    main()
