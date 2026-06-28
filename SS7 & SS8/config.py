# Cấu hình đường dẫn các file 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MAIN_UI_PATH = BASE_DIR / "ui" / "main_window.ui"
DIALOG_UI_PATH = BASE_DIR / "ui" / "anime_dialog.ui"
STYLE_PATH = BASE_DIR / "style" / "style_main.qss"
DATA_PATH = BASE_DIR / "data" / "anime_data.json"

DATE_FORMAT = "dd/MM/yyyy"
