import re


RULES = [

    ("tion", "ஷன்"),
    ("sion", "ஷன்"),

    ("ph", "ஃப்"),
    ("th", "த்"),
    ("sh", "ஷ"),
    ("ch", "ச்"),

    ("oo", "ஊ"),
    ("ee", "ஈ"),
    ("ai", "ஏ"),
    ("ay", "ஏ"),
    ("oa", "ஓ"),
    ("ou", "ஔ"),

]


LETTER_MAP = {

    "a":"அ",
    "b":"ப்",
    "c":"க்",
    "d":"ட்",
    "e":"எ",
    "f":"ஃப்",
    "g":"க்",
    "h":"ஹ்",
    "i":"இ",
    "j":"ஜ்",
    "k":"க்",
    "l":"ல்",
    "m":"ம்",
    "n":"ன்",
    "o":"ஒ",
    "p":"ப்",
    "q":"க்",
    "r":"ர்",
    "s":"ஸ்",
    "t":"ட்",
    "u":"உ",
    "v":"வ்",
    "w":"வ்",
    "x":"க்ஸ்",
    "y":"ய்",
    "z":"ஸ்",

}


def convert(word):

    text = word.lower()

    for eng, tam in RULES:
        text = text.replace(eng, tam)

    result = ""

    i = 0

    while i < len(text):

        ch = text[i]

        if ord(ch) > 127:
            result += ch
        else:
            result += LETTER_MAP.get(ch, ch)

        i += 1

    return result