STYLES = {

    "default": {
        "pitch": 1.0,
        "speed": 1.0,
        "energy": 1.0,
    },

    "news": {
        "pitch": 0.95,
        "speed": 0.95,
        "energy": 1.10,
    },

    "story": {
        "pitch": 1.05,
        "speed": 0.90,
        "energy": 0.95,
    },

    "conversation": {
        "pitch": 1.0,
        "speed": 1.0,
        "energy": 1.0,
    },

    "prayer": {
        "pitch": 0.90,
        "speed": 0.85,
        "energy": 0.80,
    },

    "advertisement": {
        "pitch": 1.10,
        "speed": 1.10,
        "energy": 1.20,
    }

}


def load(style="default"):

    return STYLES.get(
        style,
        STYLES["default"]
    )