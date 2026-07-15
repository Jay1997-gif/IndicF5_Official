import re

DIGITS = {
    "0": "பூஜ்யம்",
    "1": "ஒன்று",
    "2": "இரண்டு",
    "3": "மூன்று",
    "4": "நான்கு",
    "5": "ஐந்து",
    "6": "ஆறு",
    "7": "ஏழு",
    "8": "எட்டு",
    "9": "ஒன்பது",
}

OTP_PATTERN = re.compile(
    r"(?:OTP|otp|PIN|pin)\s*[:\-]?\s*(\d{4,8})"
)

def normalize_otp(text):

    def repl(match):
        digits = " ".join(DIGITS[d] for d in match.group(1))
        return f"ஓ டி பி {digits}"

    return OTP_PATTERN.sub(repl, text)