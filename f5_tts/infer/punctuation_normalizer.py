import re

def normalize_punctuation(text):

    text = text.replace("...", ". ")
    text = text.replace(";", ". ")
    text = text.replace(":", ". ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()