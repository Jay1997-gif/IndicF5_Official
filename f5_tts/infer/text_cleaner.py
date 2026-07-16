import re

MULTI_SPACE = re.compile(r"\s+")

def clean_text(text):

    text = text.strip()

    text = MULTI_SPACE.sub(" ", text)

    return text