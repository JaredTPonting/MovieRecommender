from src.recommendation.collaborative_filtering import get_collaborative_recommendations
from src.recommendation.content_based import get_content_recommendations

import pandas as pd


def hybrid_recommendation(title, content_weight=0.5, collaborative_weight=0.5, top_n=10):
    # Get content-based recommendations
    content_recs = get_content_recommendations(title)

    # Get collaborative recommendations
    collaborative_recs = get_collaborative_recommendations(title)

    # Combine recommendations by weighted averaging
    hybrid_recs = pd.concat([content_recs, collaborative_recs]).value_counts().index.tolist()

    # Return the top n recommendations
    return hybrid_recs[:top_n]
