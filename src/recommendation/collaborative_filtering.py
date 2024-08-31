from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

from src.data_processing.load_data import load_data

movies, _r = load_data(source='processed')

scaler = MinMaxScaler()
movies.dropna(subset=['vote_average', 'vote_count', 'popularity_metric'], inplace=True)

movies[['vote_average', 'vote_count', 'popularity_metric']] = scaler.fit_transform(
    movies[['vote_average', 'vote_count', 'popularity_metric']])

# We'll use NearestNeighbors for collaborative filtering
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(movies[['vote_average', 'vote_count', 'popularity_metric']])


# Get recommendations based on collaborative filtering
def get_collaborative_recommendations(title, df=movies, model=model_knn, top_n=10):
    idx = df[df['title'].str.lower() == title.lower()].index[0]
    distances, indices = model.kneighbors(
        df[['vote_average', 'vote_count', 'popularity_metric']].iloc[idx].values.reshape(1, -1), n_neighbors=top_n + 1)

    return df['title'].iloc[indices.flatten()[1:]]