import joblib
import pandas as pd

# Load saved pipeline
best_model = joblib.load("best_model.pkl")

# Load dataset to recover label mapping
data = pd.read_csv("Roman Urdu DataSet.csv", usecols=[0,1], names=["review", "sentiment"])
_, uniques = pd.factorize(data["sentiment"])

# Predict new review
new_review = "Mannan yera project ki report to bana"
prediction = best_model.predict([new_review])
print("Predicted sentiment:", uniques[prediction[0]])