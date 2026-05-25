import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

STOPWORDS = set(stopwords.words('english'))

def full_preprocess(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    tokens = text.split()

    filtered = []

    for token in tokens:

        if token not in STOPWORDS:

            lemma = lemmatizer.lemmatize(token)

            filtered.append(lemma)

    result = ' '.join(filtered)

    return result