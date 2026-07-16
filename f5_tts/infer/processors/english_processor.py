from ..english_normalizer import normalize_english

def process(token):
    return normalize_english(token)