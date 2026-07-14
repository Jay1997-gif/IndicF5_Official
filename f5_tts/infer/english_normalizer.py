import re

ENGLISH_MAP = {

    # Pronouns
    "i": "ஐ",
    "me": "மீ",
    "my": "மை",
    "mine": "மைன்",
    "you": "யூ",
    "your": "யுவர்",
    "he": "ஹீ",
    "she": "ஷீ",
    "we": "வீ",
    "they": "தே",

    # Common verbs
    "am": "ஆம்",
    "is": "இஸ்",
    "are": "ஆர்",
    "was": "வாஸ்",
    "were": "வேர்",
    "have": "ஹேவ்",
    "has": "ஹாஸ்",
    "had": "ஹேட்",
    "do": "டூ",
    "does": "டஸ்",
    "did": "டிட்",
    "go": "கோ",
    "come": "கம்",
    "say": "சே",
    "see": "ஸீ",
    "know": "நோ",
    "make": "மேக்",
    "take": "டேக்",

    # Time
    "today": "டுடே",
    "tomorrow": "டுமாரோ",
    "yesterday": "யெஸ்டர்டே",
    "morning": "மார்னிங்",
    "evening": "ஈவினிங்",
    "night": "நைட்",

    # Common words
    "hello": "ஹலோ",
    "hi": "ஹாய்",
    "thanks": "தேங்க்ஸ்",
    "thank": "தேங்க்",
    "please": "ப்ளீஸ்",
    "good": "குட்",
    "bad": "பேட்",
    "yes": "யெஸ்",
    "no": "நோ",

    # Money
    "rupees": "ரூபாய்",
    "rupee": "ரூபாய்",
    "dollar": "டாலர்",
    "dollars": "டாலர்",

    # Age
    "year": "யேர்",
    "years": "யேர்ஸ்",
    "old": "ஓல்ட்",

    # Tech
    "google": "கூகுள்",
    "youtube": "யூடியூப்",
    "chatgpt": "சாட் ஜிபிடி",
    "openai": "ஓபன் ஏ ஐ",
    "microsoft": "மைக்ரோசாஃப்ட்",
    "windows": "விண்டோஸ்",

}

VOWELS = {
    "a": "அ",
    "e": "எ",
    "i": "இ",
    "o": "ஒ",
    "u": "உ",
}

def transliterate_word(word):

    if word.lower() in ENGLISH_MAP:
        return ENGLISH_MAP[word.lower()]

    result = ""

    for ch in word.lower():

        if ch in VOWELS:
            result += VOWELS[ch]

        elif ch == "b":
            result += "ப்"

        elif ch == "c":
            result += "க்"

        elif ch == "d":
            result += "ட்"

        elif ch == "f":
            result += "ஃப்"

        elif ch == "g":
            result += "க்"

        elif ch == "h":
            result += "ஹ்"

        elif ch == "j":
            result += "ஜ்"

        elif ch == "k":
            result += "க்"

        elif ch == "l":
            result += "ல்"

        elif ch == "m":
            result += "ம்"

        elif ch == "n":
            result += "ன்"

        elif ch == "p":
            result += "ப்"

        elif ch == "q":
            result += "க்"

        elif ch == "r":
            result += "ர்"

        elif ch == "s":
            result += "ஸ்"

        elif ch == "t":
            result += "ட்"

        elif ch == "v":
            result += "வ்"

        elif ch == "w":
            result += "வ்"

        elif ch == "x":
            result += "க்ஸ்"

        elif ch == "y":
            result += "ய்"

        elif ch == "z":
            result += "ஸ்"

    return result

def normalize_english(text):

    def repl(match):

        word = match.group()

        return ENGLISH_MAP.get(
            word.lower(),
            word
        )

    return re.sub(
        r"[A-Za-z]+",
        repl,
        text
    )