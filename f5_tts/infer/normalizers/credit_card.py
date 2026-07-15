import re
from ..dictionaries.digits import DIGITS

CARD_PATTERN = re.compile(r"\b(?:\d{4}[- ]?){3}\d{4}\b")

def normalize_credit_card(text):

    def repl(match):
        digits = " ".join(DIGITS[d] for d in re.sub(r"\D", "", match.group()))
        return f"கிரெடிட் கார்டு {digits}"

    return CARD_PATTERN.sub(repl, text)