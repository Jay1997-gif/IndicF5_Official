import re

_DIGITS = {
    "0": "பூஜ்யம்",
    "1": "ஒன்று",
    "2": "இரண்டு",
    "3": "மூன்று",
    "4": "நான்கு",
    "5": "ஐந்து",
    "6": "ஆறு",
    "7": "ஏழு",
    "8": "எட்டு",
    "9": "ஒன்பது",
}


def _speak_digits(number):
    return " ".join(_DIGITS[d] for d in number)


def normalize_phone(text):

    def repl(match):
        phone = match.group()

        digits = re.sub(r"\D", "", phone)

        if len(digits) in (10, 11, 12):
            return _speak_digits(digits)

        return phone

    return re.sub(
        r"(\+?\d[\d\s\-]{8,}\d)",
        repl,
        text,
    )