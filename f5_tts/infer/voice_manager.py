import json
from pathlib import Path


VOICE_DIR = Path(__file__).parent / "voices"


def load(name="default"):

    path = VOICE_DIR / f"{name}.json"

    with open(path, encoding="utf-8") as f:
        return json.load(f)