def normalize_emotion(text):

    text = text.replace("!!", " !")
    text = text.replace("???", "?")
    text = text.replace("??", "?")

    return text