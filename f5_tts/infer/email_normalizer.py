import re

def normalize_email(text):

    def repl(match):

        email = match.group()

        email = email.replace("@", " அட் ")

        email = email.replace(".", " டாட் ")

        DIGITS = {
            "0": "பூஜ்ஜியம்",
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

        email = re.sub(
            r"\d",
            lambda m: " " + DIGITS[m.group()] + " ",
            email,
        )

        return re.sub(r"\s+", " ", email).strip()

    return re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        repl,
        text,
    )