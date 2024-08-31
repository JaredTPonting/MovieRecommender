import numpy as np
import pandas as pd

from src.data_processing.load_data import load_data


def main():
    movies, _ = load_data()
    movies = movies.drop('imdb_id', axis=1)
    movies = movies.drop('original_title', axis=1)
    movies['revenue'] = movies['revenue'].replace(0, np.nan)
    movies['budget'] = pd.to_numeric(movies['budget'], errors='coerce')
    movies['budget'] = movies['budget'].replace(0, np.nan)
    movies['release_year'] = pd.to_datetime(movies['release_date'], errors='coerce').dt.year
    movies = movies.sort_values('vote_count', ascending=False).drop_duplicates(subset=['id', 'title'], keep='first')
    movies.to_csv('../../data/preprocessing/movies_metadata.csv')


if __name__ == "__main__":
    main()
