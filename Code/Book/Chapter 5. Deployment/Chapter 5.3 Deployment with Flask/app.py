from flask import Flask, request, jsonify, render_template
import numpy as np
from joblib import load

app = Flask(__name__)
spicies_map = {1: 'Adelie', 2: 'Gentoo'}

@app.before_first_request
def load_model_to_app():
    """Load model before any other actions."""
    app.model = load('./static/model/classifier.joblib')

@app.route("/")
def index():
    """In the home route just load index."""
    return render_template('index.html', pred = 0)

@app.route('/predict', methods=['POST'])
def predict():
    """Provide main prediction API route. Responds to both GET and POST requests."""
    data = [request.form['culmen_length'], request.form['culmen_depth']]

    data = np.array([np.asarray(data, dtype=float)])
    
    species = app.model.predict(data)

    print('INFO Predictions: {}'.format(spicies_map[species[0]]))

    return render_template('index.html', pred=spicies_map[species[0]])

def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000, debug=False)  # nosec


if __name__ == '__main__':
    main()