import re
from ..dictionaries.digits import DIGITS

OTP_PATTERN = re.compile(
    r"(?:OTP|otp|PIN|pin)\s*[:\-]?\s*(\d{4,8})"
)

def normalize_otp(text):

    def repl(match):
        digits = " ".join(DIGITS[d] for d in match.group(1))
        return f"ஓ டி பி {digits}"

    return OTP_PATTERN.sub(repl, text)