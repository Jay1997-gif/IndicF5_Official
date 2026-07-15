import re

DIGITS = {
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

AADHAAR_PATTERN = re.compile(r"\b(?:\d{4}\s?){2}\d{4}\b")

def normalize_aadhaar(text):

    def repl(match):
        digits = " ".join(DIGITS[d] for d in re.sub(r"\D", "", match.group()))
        return f"ஆதார் எண் {digits}"

    return AADHAAR_PATTERN.sub(repl, text)