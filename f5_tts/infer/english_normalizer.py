import re

from .dictionaries.english_words import WORDS
from .dictionaries.brands import BRANDS
from .dictionaries.acronyms import ACRONYMS

ENGLISH_MAP = {}

ENGLISH_MAP.update(WORDS)
ENGLISH_MAP.update(BRANDS)

for k, v in ACRONYMS.items():
    ENGLISH_MAP[k.lower()] = v
VOWELS = {
    "a": "அ",
    "e": "எ",
    "i": "இ",
    "o": "ஒ",
    "u": "உ",
}

def transliterate_word(word):

    if word.lower() in ENGLISH_MAP:
        return ENGLISH_MAP[word.lower()]

    result = ""

    for ch in word.lower():

        if ch in VOWELS:
            result += VOWELS[ch]

        elif ch == "b":
            result += "ப்"

        elif ch == "c":
            result += "க்"

        elif ch == "d":
            result += "ட்"

        elif ch == "f":
            result += "ஃப்"

        elif ch == "g":
            result += "க்"

        elif ch == "h":
            result += "ஹ்"

        elif ch == "j":
            result += "ஜ்"

        elif ch == "k":
            result += "க்"

        elif ch == "l":
            result += "ல்"

        elif ch == "m":
            result += "ம்"

        elif ch == "n":
            result += "ன்"

        elif ch == "p":
            result += "ப்"

        elif ch == "q":
            result += "க்"

        elif ch == "r":
            result += "ர்"

        elif ch == "s":
            result += "ஸ்"

        elif ch == "t":
            result += "ட்"

        elif ch == "v":
            result += "வ்"

        elif ch == "w":
            result += "வ்"

        elif ch == "x":
            result += "க்ஸ்"

        elif ch == "y":
            result += "ய்"

        elif ch == "z":
            result += "ஸ்"

    return result

def normalize_english(text):

    def repl(match):

        word = match.group()

        return ENGLISH_MAP.get(
            word.lower(),
            word
        )

    return re.sub(
        r"[A-Za-z]+",
        repl,
        text
    )