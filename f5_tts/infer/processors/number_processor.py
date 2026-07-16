from ..normalizers.number import normalize_numbers

def process(token):
    return normalize_numbers(token)