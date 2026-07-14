from .normalizers.number import normalize_numbers
from .normalizers.phone import normalize_phone
from .date_normalizer import normalize_dates
from .time_normalizer import normalize_time
from .percentage_normalizer import normalize_percentage
from .email_normalizer import normalize_email
from .currency_normalizer import normalize_currency
from .unit_normalizer import normalize_units
from .english_normalizer import normalize_english
from .punctuation_normalizer import normalize_punctuation
from .emotion_normalizer import normalize_emotion

def preprocess(text):

    text = normalize_dates(text)

    text = normalize_time(text)

    text = normalize_percentage(text)

    text = normalize_email(text)

    text = normalize_currency(text)

    text = normalize_units(text)

    text = normalize_phone(text)

    text = normalize_numbers(text)

    text = normalize_english(text)

    text = normalize_punctuation(text)

    text = normalize_emotion(text)

    return text