import pickle
import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences

from app.utils.preprocessing import full_preprocess

from app.services.translation_service import (
    translate_to_english
)

MAX_LEN = 60

model = tf.keras.models.load_model(
    "app/models/model.keras"
)

with open(
    "app/models/tokenizer.pkl",
    "rb"
) as f:

    tokenizer = pickle.load(f)

with open(
    "app/models/label_encoder.pkl",
    "rb"
) as f:

    label_encoder = pickle.load(f)

def classify_journal(text):

    translated_text = translate_to_english(
        text
    )

    cleaned_text = full_preprocess(
        translated_text
    )

    sequence = tokenizer.texts_to_sequences(
        [cleaned_text]
    )

    padded = pad_sequences(
        sequence,
        maxlen=MAX_LEN,
        padding='post'
    )

    prediction = model.predict(
        padded,
        verbose=0
    )[0]

    predicted_index = np.argmax(prediction)

    label = label_encoder.classes_[
        predicted_index
    ]

    confidence = float(
        prediction[predicted_index]
    )

    return {
        "original_text": text,
        "translated_text": translated_text,
        "cleaned_text": cleaned_text,
        "label": label,
        "confidence": confidence
    }