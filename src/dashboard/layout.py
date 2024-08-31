from dash import html, dcc


def create_layout():
    return html.Div([
        html.H1("Movie Recommendation System"),
        dcc.Input(id='input-movie', type='text', placeholder='Enter a movie title', debounce=True),
        dcc.RadioItems(
            id='model-type',
            options=[
                {'label': 'Content-Based', 'value': 'content'},
                {'label': 'Collaborative Filtering', 'value': 'collaborative'},
                {'label': 'Hybrid', 'value': 'hybrid'}
            ],
            value='hybrid',
            labelStyle={'display': 'inline-block'}
        ),
        html.Button('Get Recommendations', id='submit-button', n_clicks=0),
        html.Div(id='output-recommendations')
    ])
