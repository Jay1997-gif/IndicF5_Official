import json
from pathlib import Path

CUSTOM = {}

BASE_DIR = Path(__file__).parent
DICT_FILE = BASE_DIR / "phonemes" / "phonemes.json"


def load_dictionary():

    if not DICT_FILE.exists():
        return {}

    with open(DICT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


WORDS = load_dictionary()


def register(word, phoneme):

    CUSTOM[word.lower()] = phoneme


def get(word):

    key = word.lower()

    if key in CUSTOM:
        return CUSTOM[key]

    if key in WORDS:
        return WORDS[key]

    return None