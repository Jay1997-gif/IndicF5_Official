from ..normalizers.number import normalize_numbers
from ..processor_registry import register

register("NUMBER", process)

def process(token):
    return normalize_numbers(token)