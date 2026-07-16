import re


def analyze(token):

    if re.fullmatch(r"\d+", token):
        return "NUMBER"

    if re.fullmatch(r"₹", token):
        return "CURRENCY"

    if re.fullmatch(r"%", token):
        return "PERCENT"

    if re.fullmatch(r"[A-Za-z]+", token):
        return "ENGLISH"

    return "TEXT"