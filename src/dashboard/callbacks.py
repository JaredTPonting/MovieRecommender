from dash import Input, Output, State, html
from dash.exceptions import PreventUpdate
import data_interface


def register_callbacks(app):
    @app.callback(
        Output('output-recommendations', 'children'),
        Input('submit-button', 'n_clicks'),
        State('input-movie', 'value'),
        State('model-type', 'value')
    )
    def update_recommendations(n_clicks, movie_title, model_type):
        if n_clicks == 0 or not movie_title:
            raise PreventUpdate

        recommendations = data_interface.get_recommendations(movie_title, model_type)

        return html.Ul([html.Li(rec) for rec in recommendations])
