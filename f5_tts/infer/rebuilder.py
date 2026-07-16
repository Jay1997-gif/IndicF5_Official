PUNCTUATION = {
    ".",
    ",",
    "!",
    "?",
    ":",
    ";",
    ")",
    "]",
    "}",
}

def rebuild(tokens):

    output = ""

    for token in tokens:

        if not output:
            output = token

        elif token in PUNCTUATION:
            output += token

        else:
            output += " " + token

    return output