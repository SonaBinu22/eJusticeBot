import json
import random
import nltk
import string

# Safe download of punkt
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from nltk.tokenize import word_tokenize

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def preprocess(text):
    # Lowercase, remove punctuation, tokenize
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(text)
    return tokens

def get_response(user_input):
    tokens = preprocess(user_input)
    best_match = None
    max_overlap = 0

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = preprocess(pattern)
            overlap = len(set(tokens) & set(pattern_tokens))
            if overlap > max_overlap:
                max_overlap = overlap
                best_match = intent

    if best_match and max_overlap > 0:
        response = random.choice(best_match["responses"])
        return response
    else:
        return "I'm sorry, I couldn't understand that. Could you please rephrase your question?"

