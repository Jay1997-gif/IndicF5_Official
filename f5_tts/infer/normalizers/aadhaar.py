import re
from ..dictionaries.digits import DIGITS

AADHAAR_PATTERN = re.compile(r"\b(?:\d{4}\s?){2}\d{4}\b")

def normalize_aadhaar(text):

    def repl(match):
        digits = " ".join(DIGITS[d] for d in re.sub(r"\D", "", match.group()))
        return f"ஆதார் எண் {digits}"

    return AADHAAR_PATTERN.sub(repl, text)