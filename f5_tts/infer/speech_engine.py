from .pipeline import run_pipeline
from .speech_features import extract
from .voice_config import build


def prepare(
    text,
    voice="default",
    style="default"
):

    normalized = run_pipeline(text)

    features = extract(normalized)

    config = build(
        voice=voice,
        style=style
    )

    return {
        "text": normalized,
        "features": features,
        "voice": config,
    }