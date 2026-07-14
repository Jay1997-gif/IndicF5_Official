import re
from f5_tts.infer.number_normalizer import tamil_number

def normalize_units(text):

    text = re.sub(
        r"(\d+)\s?km\b",
        lambda m:
        tamil_number(int(m.group(1))) + " கிலோமீட்டர்",
        text,
        flags=re.I
    )

    text = re.sub(
        r"(\d+)\s?kg\b",
        lambda m:
        tamil_number(int(m.group(1))) + " கிலோகிராம்",
        text,
        flags=re.I
    )

    return text