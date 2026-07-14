import re

from .number_normalizer import tamil_number


def normalize_percentage(text):

    text = re.sub(
        r"(\d+)\s?%",
        lambda m: tamil_number(int(m.group(1))) + " சதவீதம்",
        text,
    )

    return text