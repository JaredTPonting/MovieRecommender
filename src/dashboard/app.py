from dash import Dash
import layout
import callbacks

# Initialize the Dash app
app = Dash(__name__)

# Set up the layout
app.layout = layout.create_layout()

# Register callbacks
callbacks.register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
