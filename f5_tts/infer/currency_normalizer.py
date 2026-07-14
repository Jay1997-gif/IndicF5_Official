import re
from f5_tts.infer.number_normalizer import tamil_number

def normalize_currency(text):

    text = re.sub(
        r"₹\s?(\d+)",
        lambda m:
        tamil_number(int(m.group(1))) + " ரூபாய்",
        text
    )

    return text