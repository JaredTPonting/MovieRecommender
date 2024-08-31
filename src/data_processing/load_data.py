import os

import pandas as pd


def load_data(source='raw'):

    base_dir = os.path.dirname(os.path.abspath(__file__))

    rating_path = os.path.join(base_dir, "..", "..", "data", "raw", "ratings.csv")
    ratings = pd.read_csv(rating_path)

    movies_path = os.path.join(base_dir, "..", "..", "data", f"{source}", "movies_metadata.csv")
    movies = pd.read_csv(movies_path)

    return movies, ratings
