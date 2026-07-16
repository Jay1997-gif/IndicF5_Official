from .voice_manager import load as load_voice
from .style_engine import load as load_style


def build(
    voice="default",
    style="default"
):

    voice_cfg = load_voice(voice)

    style_cfg = load_style(style)

    config = voice_cfg.copy()

    config.update(style_cfg)

    return config