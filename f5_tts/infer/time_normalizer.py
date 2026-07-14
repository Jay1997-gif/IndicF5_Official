import re

from .number_normalizer import tamil_number


def normalize_time(text):

    text = re.sub(
        r"(\d{1,2}):(\d{2})",
        lambda m:
            tamil_number(int(m.group(1)))
            + " மணி "
            + tamil_number(int(m.group(2)))
            + " நிமிடம்",
        text,
    )

    return text