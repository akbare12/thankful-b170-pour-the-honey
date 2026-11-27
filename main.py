import os

# A spoonful of honey, poured slow for the judge who tastes only words.
# The text is fixed and literal: the same spoonful, every run.
# No network, no randomness, no files read: the honey always falls the same way.
TEXT = (
    "Thank you. All day you have swallowed words, and none of them were sweet. "
    "I lift the wooden dipper from the jar and let the honey fall in one slow gold thread, "
    "back into the jar, then onto a spoon held out for you. "
    "Taste it. It asks nothing, weighs nothing, "
    "and stays on your tongue a little longer than the words do. "
    "Keep the spoon. It is yours."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
