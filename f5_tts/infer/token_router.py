from .token_classifier import classify


def route(token):

    token_type = classify(token)

    if token_type == "TAMIL":
        return ("tamil", token)

    elif token_type == "ENGLISH":
        return ("english", token)

    elif token_type == "NUMBER":
        return ("number", token)

    return ("other", token)