import pickle
import re
from pathlib import Path

__version__ = "01"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/sa_pipeline_{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


classes = [
    "negative",
    "positive"
]


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    return classes[pred[0]]
