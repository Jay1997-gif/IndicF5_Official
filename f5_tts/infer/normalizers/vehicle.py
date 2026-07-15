import re

VEHICLE_PATTERN = re.compile(
    r"\b[A-Z]{2}\s?\d{2}\s?[A-Z]{1,2}\s?\d{4}\b"
)

def normalize_vehicle(text):
    return VEHICLE_PATTERN.sub(
        lambda m: "வாகன எண் " + " ".join(m.group().replace(" ", "")),
        text
    )