from .token_classifier import classify

from .processors.tamil_processor import process as tamil_process
from .processors.english_processor import process as english_process
from .processors.number_processor import process as number_process
from .processors.other_processor import process as other_process


def route(token):

    token_type = classify(token)

    if token_type == "TAMIL":
        return tamil_process(token)

    elif token_type == "ENGLISH":
        return english_process(token)

    elif token_type == "NUMBER":
        return number_process(token)

    return other_process(token)