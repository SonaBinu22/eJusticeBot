import json
import random
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

nltk.download('punkt')

with open('intents.json') as file:
    data = json.load(file)

# Prepare training data
corpus = []
tags = []
for intent in data['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        tags.append(intent['tag'])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = np.array(tags)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

# Response function
def get_response(user_input):
    with open('intents.json') as file:
        data = json.load(file)

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    X = vectorizer.transform([user_input])
    tag = model.predict(X)[0]

    for intent in data['intents']:
        if intent['tag'] == tag:
            return "\n".join(intent['responses'])

    return "Sorry, I didn’t understand. Please rephrase your question."
