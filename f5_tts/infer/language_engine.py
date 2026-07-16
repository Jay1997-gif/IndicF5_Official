import re


def detect(token):

    if re.fullmatch(r"[A-Za-z0-9\-\._]+", token):
        return "ENGLISH"

    if re.search(r"[\u0B80-\u0BFF]", token):
        return "TAMIL"

    return "UNKNOWN"