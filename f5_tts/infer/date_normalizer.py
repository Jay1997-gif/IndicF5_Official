import re
from f5_tts.infer.number_normalizer import tamil_number

def normalize_dates(text):

    text = re.sub(
        r"(\d{1,2})/(\d{1,2})/(\d{4})",
        lambda m:
        f"{tamil_number(int(m.group(1)))} "
        f"{tamil_number(int(m.group(2)))} "
        f"{tamil_number(int(m.group(3)))}",
        text
    )

    return text