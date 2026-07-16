from .emotion_engine import detect

def analyze(text):

    result = {
        "pause": False,
        "question": False,
        "exclamation": False,
        "emotion": detect(text)
    }

    if "?" in text:
        result["question"] = True

    if "!" in text:
        result["exclamation"] = True

    if "." in text:
        result["pause"] = True

    return result