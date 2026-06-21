import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


BASE_DIR = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_path = BASE_DIR / "ui" / "main_window.ui"
        qss_path = BASE_DIR / "ui" / "style_main.qss"

        uic.loadUi(ui_path, self)

        with open(qss_path, "r", encoding="utf-8") as file:
            self.setStyleSheet(file.read())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())