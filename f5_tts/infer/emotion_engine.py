HAPPY = [
    "வாழ்த்துக்கள்",
    "சந்தோஷம்",
    "அருமை",
    "சூப்பர்",
    "நன்றி",
]

SAD = [
    "வருத்தம்",
    "கவலை",
    "துக்கம்",
]

ANGRY = [
    "கோபம்",
    "முட்டாள்",
]

def detect(text):

    t = text.lower()

    for word in HAPPY:
        if word in t:
            return "happy"

    for word in SAD:
        if word in t:
            return "sad"

    for word in ANGRY:
        if word in t:
            return "angry"

    return "neutral"