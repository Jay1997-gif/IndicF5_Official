from .date_normalizer import normalize_dates
from .time_normalizer import normalize_time
from .percentage_normalizer import normalize_percentage
from .normalizers.url import normalize_url
from .email_normalizer import normalize_email
from .currency_normalizer import normalize_currency
from .unit_normalizer import normalize_units
from .normalizers.phone import normalize_phone
from .normalizers.number import normalize_numbers
from .english_normalizer import normalize_english
from .punctuation_normalizer import normalize_punctuation
from .emotion_normalizer import normalize_emotion

PIPELINE = [
    normalize_dates,
    normalize_time,
    normalize_percentage,
    normalize_url,
    normalize_email,
    normalize_currency,
    normalize_units,
    normalize_phone,
    normalize_numbers,
    normalize_english,
    normalize_punctuation,
    normalize_emotion,
]

def run_pipeline(text):
    for step in PIPELINE:
        text = step(text)
    return text