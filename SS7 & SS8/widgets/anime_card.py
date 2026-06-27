from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QLabel, QWidget, QHBoxLayout, QVBoxLayout

from config import BASE_DIR


class AnimeCard(QFrame):
    """
    Widget card hiển thị thông tin anime ở trang Home.
    Gồm: ảnh, tên, ngày phát hành, rating.
    """

    def __init__(self, anime):
        super().__init__()

        self.anime = anime

        self.setObjectName("animeCard")
        self.setFixedHeight(135)

        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)

        image_label = QLabel()
        image_label.setObjectName("animeCardImage")
        image_label.setFixedSize(95, 115)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.set_image(image_label, self.anime.get("image", ""))

        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(6)

        title_label = QLabel(self.anime.get("title", "Unknown"))
        title_label.setObjectName("animeCardTitle")
        title_label.setWordWrap(True)

        date_label = QLabel(f"Release Date: {self.anime.get('release_date', '')}")
        date_label.setObjectName("animeCardText")

        rating_label = QLabel(f"Rating: {self.anime.get('rating', 0)}")
        rating_label.setObjectName("animeCardText")

        info_layout.addWidget(title_label)
        info_layout.addWidget(date_label)
        info_layout.addWidget(rating_label)
        info_layout.addStretch()

        layout.addWidget(image_label)
        layout.addWidget(info_widget)

    def set_image(self, label, image_path):
        """
        Gán ảnh vào QLabel.
        Nếu image_path là đường dẫn tương đối, ví dụ img/banner.png,
        chương trình sẽ tự hiểu là BASE_DIR/img/banner.png.
        """

        if not image_path:
            label.setText("No Image")
            return

        image_path = Path(image_path)

        if not image_path.is_absolute():
            image_path = BASE_DIR / image_path

        pixmap = QPixmap(str(image_path))

        if pixmap.isNull():
            label.setText("No Image")
            return

        pixmap = pixmap.scaled(
            label.width(),
            label.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        label.setPixmap(pixmap)
