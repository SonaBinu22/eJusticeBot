import random
import json
import nltk
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Load intents JSON
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# NLP preprocessing
lemmatizer = WordNetLemmatizer()
corpus = []
labels = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern)
        tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens]
        corpus.append(" ".join(tokens))
        labels.append(intent["tag"])

    responses[intent["tag"]] = intent["responses"]

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Response function
def get_response(user_input):
    tokens = nltk.word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(w.lower()) for w in tokens]
    X_test = vectorizer.transform([" ".join(tokens)])
    tag = model.predict(X_test)[0]

    if tag in responses:
        return random.choice(responses[tag])
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"

