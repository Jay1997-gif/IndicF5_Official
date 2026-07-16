import re

TAMIL = re.compile(r'^[\u0B80-\u0BFF]+$')
ENGLISH = re.compile(r'^[A-Za-z]+$')
NUMBER = re.compile(r'^\d+$')

def classify(token):

    if TAMIL.match(token):
        return "TAMIL"

    if ENGLISH.match(token):
        return "ENGLISH"

    if NUMBER.match(token):
        return "NUMBER"

    return "OTHER"