from pathlib import Path

from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDialog, QMessageBox, QFileDialog

from config import DIALOG_UI_PATH, DATE_FORMAT


class AnimeDialog(QDialog):
    """
    Dialog dùng cho cả Add và Edit anime.
    """

    def __init__(self, parent=None, anime=None):
        super().__init__(parent)

        uic.loadUi(DIALOG_UI_PATH, self)

        self.image_path = ""
        self.setWindowTitle("Anime Dialog")

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat(DATE_FORMAT)

        if hasattr(self, "btnAddFile"):
            self.btnAddFile.clicked.connect(self.choose_image)

        if anime is not None:
            self.load_anime(anime)

    def load_anime(self, anime):
        """
        Đổ dữ liệu anime cũ lên form khi Edit.
        """

        self.inputTitle.setText(anime.get("title", ""))
        self.inputRating.setText(str(anime.get("rating", "")))
        self.inputLink.setText(anime.get("link", ""))

        self.image_path = anime.get("image", "")

        date = QDate.fromString(anime.get("release_date", ""), DATE_FORMAT)

        if date.isValid():
            self.dateEdit.setDate(date)

        if self.image_path and hasattr(self, "btnAddFile"):
            self.btnAddFile.setText(Path(self.image_path).name)

    def choose_image(self):
        """
        Mở hộp thoại chọn ảnh.
        """

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Chọn ảnh anime",
            "",
            "Image Files (*.png *.jpg *.jpeg *.webp *.svg)"
        )

        if file_path:
            self.image_path = file_path
            self.btnAddFile.setText(Path(file_path).name)

    def get_data(self):
        """
        Lấy dữ liệu từ form và trả về dictionary.
        """

        title = self.inputTitle.text().strip()
        rating_text = self.inputRating.text().strip()

        if not title:
            QMessageBox.warning(self, "Lỗi", "Tên anime không được để trống.")
            return None

        try:
            rating = float(rating_text) if rating_text else 0
        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Rating phải là số.")
            return None

        return {
            "title": title,
            "release_date": self.dateEdit.date().toString(DATE_FORMAT),
            "image": self.image_path,
            "rating": rating,
            "link": self.inputLink.text().strip()
        }
