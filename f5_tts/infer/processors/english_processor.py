from ..english_normalizer import normalize_english
from ..processor_registry import register

register("ENGLISH", process)

def process(token):
    return normalize_english(token)