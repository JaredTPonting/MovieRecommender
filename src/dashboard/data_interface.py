from src.recommendation.hybrid_model import hybrid_recommendation
from src.recommendation.content_based import get_content_recommendations
from src.recommendation.collaborative_filtering import get_collaborative_recommendations


def get_recommendations(movie_title, model_type):
    if model_type == 'content':
        return get_content_recommendations(movie_title)
    elif model_type == 'collaborative':
        return get_collaborative_recommendations(movie_title)
    elif model_type == 'hybrid':
        return hybrid_recommendation(movie_title)
