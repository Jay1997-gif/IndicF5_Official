from .language_engine import detect
from .pronunciation_engine import pronounce


def process(token):

    lang = detect(token)

    if lang == "ENGLISH":
        return pronounce(token)

    return token