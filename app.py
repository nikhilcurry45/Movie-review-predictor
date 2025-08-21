from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load model + vectorizer
model = joblib.load("movie_review_predictor\\sentiment_model.pkl")
vectorizer = joblib.load("movie_review_predictor\\vectorizer.pkl")

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
