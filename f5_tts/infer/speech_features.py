from .prosody_engine import analyze


def extract(text):

    return {
        "text": text,
        "prosody": analyze(text)
    }