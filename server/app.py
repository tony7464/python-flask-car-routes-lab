from flask import Flask

# Flask app instance — all routes attach to this object
app = Flask(__name__)

# Fleet catalog used by the /<model> lookup
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    """GET / — company welcome message."""
    return "Welcome to Flatiron Cars"


@app.route('/<model>')
def car_model(model):
    """GET /<model> — report whether the requested model is in the fleet."""
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'
