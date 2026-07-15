import re

PAN_PATTERN = re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")

def normalize_pan(text):
    return PAN_PATTERN.sub(lambda m: "பேன் எண் " + " ".join(m.group()), text)