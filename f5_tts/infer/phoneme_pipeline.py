from .phoneme_converter import convert


def build(text):

    words = text.split()

    phonemes = []

    for word in words:
        phonemes.append(
            convert(word)
        )

    return phonemes