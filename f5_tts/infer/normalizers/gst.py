import re

GST_PATTERN = re.compile(r"\b\d{2}[A-Z]{5}\d{4}[A-Z][A-Z0-9]Z[A-Z0-9]\b")

def normalize_gst(text):
    return GST_PATTERN.sub(
        lambda m: "ஜி எஸ் டி எண் " + " ".join(m.group()),
        text
    )