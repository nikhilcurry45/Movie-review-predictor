from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib
df = pd.read_csv("movie_review_predictor\IMDB Dataset.csv")
msgs = np.array(df["review"])

model = LogisticRegression()

le = LabelEncoder()
df["S_encoded"] = le.fit_transform(df["sentiment"])
y = np.array(df["S_encoded"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(msgs)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2,random_state=42)

model.fit(X_train,y_train)

joblib.dump(model,'sentiment_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print('model and vectorizer saved successfully')