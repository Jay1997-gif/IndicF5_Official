import re

IFSC_PATTERN = re.compile(r"\b[A-Z]{4}0[A-Z0-9]{6}\b")

def normalize_ifsc(text):
    return IFSC_PATTERN.sub(
        lambda m: "ஐ எப் எஸ் சி " + " ".join(m.group()),
        text
    )