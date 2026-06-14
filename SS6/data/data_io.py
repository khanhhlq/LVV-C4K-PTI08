# Thêm thư viện JSON
import json
# Thư viện đường dẫn
from pathlib import Path

# Tạo đường file data: data.json
DATA_FILE = Path(__file__).parent / "data.json"

# Hàm load data
def load_json_data():
    with open(DATA_FILE, "r", encoding="utf-8") as json_in:
        return json.load(json_in)

# Hàm write data
def write_json_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as json_out:
        json.dump(data, json_out, indent=4, ensure_ascii=False)