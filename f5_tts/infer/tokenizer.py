import re

PUNCTUATION = ".,!?;:()[]{}\"'"

def tokenize(text):

    tokens = []

    current = ""

    for ch in text:

        if ch.isspace():

            if current:
                tokens.append(current)
                current = ""

        elif ch in PUNCTUATION:

            if current:
                tokens.append(current)
                current = ""

            tokens.append(ch)

        else:
            current += ch

    if current:
        tokens.append(current)

    return tokens