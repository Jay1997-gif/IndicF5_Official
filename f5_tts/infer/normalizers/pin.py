import re
from ..dictionaries.digits import DIGITS

PIN_PATTERN = re.compile(r"(?:PIN|Pin|pin)\s*[:\-]?\s*(\d{4,6})")

def normalize_pin(text):
    def repl(match):
        digits = " ".join(DIGITS[d] for d in match.group(1))
        return f"பின் {digits}"

    return PIN_PATTERN.sub(repl, text)