import re

PASSPORT_PATTERN = re.compile(r"\b[A-Z][0-9]{7}\b")

def normalize_passport(text):
    return PASSPORT_PATTERN.sub(
        lambda m: "பாஸ்போர்ட் எண் " + " ".join(m.group()),
        text
    )