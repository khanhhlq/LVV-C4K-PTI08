import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"

def load_json_data():
    with open(DATA_FILE, "r", encoding="utf-8") as json_in:
        return json.load(json_in)

def write_json_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as json_out:
        json.dump(data, json_out, indent=4, ensure_ascii=False)