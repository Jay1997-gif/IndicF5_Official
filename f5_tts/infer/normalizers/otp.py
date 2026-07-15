import re

from .number import DIGITS

OTP_PATTERN = re.compile(r"\b\d{4,8}\b")


def normalize_otp(text):
    return text