from .auto_register import auto_register

auto_register()

from .context_analyzer import analyze
from .processor_registry import get


def process_token(token):

    token_type = analyze(token)

    processor = get(token_type)

    if processor is None:
        return token

    return processor(token)