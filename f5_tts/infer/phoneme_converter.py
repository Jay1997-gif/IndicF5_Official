from .phoneme_engine import get

def convert(word):

    phoneme = get(word)

    if phoneme is not None:
        return phoneme

    return word