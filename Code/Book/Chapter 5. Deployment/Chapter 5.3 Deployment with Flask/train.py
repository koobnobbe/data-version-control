import pandas as pd
import numpy as np
from joblib import dump

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and preprocess data.
data = pd.read_csv('./data/penguins_size.csv')

data = data.dropna()
data = data.drop(['sex', 'island', 'flipper_length_mm', 'body_mass_g'], axis=1)
data = data[data['species'] != 'Chinstrap']

X = data.drop(['species'], axis=1).values

y = data['species']
species = {'Adelie': 1, 'Gentoo': 2}
y = [species[item] for item in y]
y = np.array(y) 

X = np.delete(X, 182, axis=0)
y = np.delete(y, 182, axis=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)

# Train model.
model = RandomForestClassifier(n_estimators=11, max_leaf_nodes=16, n_jobs=-1)
model.fit(X_train, y_train)

# Save model into file.
dump(model, './static/model/classifier.joblib')