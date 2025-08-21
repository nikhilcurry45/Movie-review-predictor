from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

Base_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(Base_DIR, "sentiment_model.pkl"))
vectorizer = joblib.load(os.path.join(Base_DIR, "vectorizer.pkl"))

# Serve HTML page
@app.route("/")
def home():
    return render_template("index.html")

# API for prediction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("review", "")

    if review.strip() == "":
        return jsonify({"error": "Empty review"}), 400

    val = vectorizer.transform([review])
    prediction = model.predict(val)[0]
    sentiment = "Positive 😀" if prediction == 1 else "Negative 😞"

    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
