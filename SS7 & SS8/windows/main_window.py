from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QScrollArea
)

from config import MAIN_UI_PATH, STYLE_PATH, DATA_PATH, DATE_FORMAT
from models import AnimeDatabase
from dialogs.anime_dialog import AnimeDialog
from widgets.anime_card import AnimeCard


class MainWindow(QMainWindow):
    """
    Cửa sổ chính của app.
    """

    def __init__(self):
        super().__init__()

        uic.loadUi(MAIN_UI_PATH, self)

        self.db = AnimeDatabase(DATA_PATH)
        self.db.load_data()

        self.load_style()
        self.setup_home()
        self.connect_events()
        self.load_data()

    # =========================
    # SETUP
    # =========================

    def load_style(self):
        if STYLE_PATH.exists():
            self.setStyleSheet(STYLE_PATH.read_text(encoding="utf-8"))

    def setup_home(self):
        """
        Tạo vùng hiển thị danh sách card anime ở Home.
        """

        if hasattr(self, "labelHomeImage"):
            self.labelHomeImage.hide()

        self.homeScroll = QScrollArea()
        self.homeScroll.setWidgetResizable(True)
        self.homeScroll.setObjectName("homeScrollArea")

        self.homeContainer = QWidget()
        self.homeContainer.setObjectName("homeAnimeContainer")

        self.homeLayout = QVBoxLayout(self.homeContainer)
        self.homeLayout.setContentsMargins(10, 10, 10, 10)
        self.homeLayout.setSpacing(12)

        self.homeScroll.setWidget(self.homeContainer)

        self.pageHome.layout().addWidget(self.homeScroll)

    def connect_events(self):
        """
        Kết nối button với hàm xử lý.
        """

        self.stackedWidget.setCurrentIndex(0)

        self.btnHome.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnRankings.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btnManage.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btnExit.clicked.connect(self.close)

        self.btnAdd.clicked.connect(self.add_anime)
        self.btnEdit.clicked.connect(self.edit_anime)
        self.btnDelete.clicked.connect(self.delete_anime)
        self.btnSearch.clicked.connect(self.search_anime)

        self.btnTopAnime.clicked.connect(lambda: self.show_rank("rating"))
        self.btnLatest.clicked.connect(lambda: self.show_rank("latest"))
        self.btnAZ.clicked.connect(lambda: self.show_rank("az"))

        self.inputSearchManage.textChanged.connect(self.filter_manage)
        self.inputSearchHome.textChanged.connect(self.filter_home)

    # =========================
    # LOAD DATA
    # =========================

    def load_data(self):
        self.db.load_data()

        anime_list = self.db.get_all_items()

        self.show_list(self.animeList, anime_list)
        self.show_list(self.animeRankingList, anime_list)
        self.show_home_cards(anime_list)

    def show_list(self, list_widget, anime_list):
        list_widget.clear()

        for anime in anime_list:
            list_widget.addItem(self.format_item(anime))

    def format_item(self, anime):
        return f"{anime['title']} | {anime['release_date']} | Rating: {anime['rating']}"

    # =========================
    # CRUD
    # =========================

    def add_anime(self):
        dialog = AnimeDialog(self)

        if dialog.exec():
            data = dialog.get_data()

            if data:
                self.db.add_item(data)
                self.refresh()

    def edit_anime(self):
        title = self.selected_title()

        if not title:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn anime cần sửa.")
            return

        anime = self.db.get_first_item_by_title(title)

        if not anime:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy anime.")
            return

        dialog = AnimeDialog(self, anime)

        if dialog.exec():
            data = dialog.get_data()

            if data:
                self.db.edit_item(title, data)
                self.refresh()

    def delete_anime(self):
        title = self.selected_title()

        if not title:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn anime cần xóa.")
            return

        confirm = QMessageBox.question(
            self,
            "Remove Anime",
            f"Bạn có chắc muốn xóa anime '{title}' không?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirm == QMessageBox.StandardButton.Yes:
            self.db.delete_item(title)
            self.refresh()

    def selected_title(self):
        row = self.animeList.currentRow()

        if row == -1:
            return None

        return self.animeList.item(row).text().split("|")[0].strip()

    def refresh(self):
        self.inputSearchManage.clear()
        self.inputSearchHome.clear()
        self.load_data()

    # =========================
    # SEARCH
    # =========================

    def filter_manage(self):
        keyword = self.inputSearchManage.text().lower().strip()

        for i in range(self.animeList.count()):
            item = self.animeList.item(i)
            item.setHidden(keyword != "" and keyword not in item.text().lower())

    def search_anime(self):
        keyword = self.inputSearchManage.text().lower().strip()

        if not keyword:
            QMessageBox.information(self, "Search Result", "Vui lòng nhập tên anime cần tìm.")
            return

        results = self.db.search_by_title(keyword)

        if not results:
            QMessageBox.information(self, "Search Result", "Không tìm thấy anime nào phù hợp.")
            return

        QMessageBox.information(self, "Search Result", self.format_search_result(results))

    def format_search_result(self, results):
        text = ""

        for anime in results:
            text += (
                f"Tên: {anime['title']}\n"
                f"Ngày phát hành: {anime['release_date']}\n"
                f"Rating: {anime['rating']}\n"
                f"Image: {anime.get('image', '')}\n"
                f"Link: {anime['link']}\n"
                f"-------------------------\n"
            )

        return text

    # =========================
    # HOME
    # =========================

    def show_home_cards(self, anime_list):
        self.clear_layout(self.homeLayout)

        for anime in anime_list:
            self.homeLayout.addWidget(AnimeCard(anime))

        self.homeLayout.addStretch()

    def filter_home(self):
        keyword = self.inputSearchHome.text().lower().strip()

        anime_list = [
            anime for anime in self.db.get_all_items()
            if keyword in anime["title"].lower()
        ]

        self.show_home_cards(anime_list)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

    # =========================
    # RANKING
    # =========================

    def show_rank(self, mode):
        anime_list = self.db.get_all_items()

        if mode == "rating":
            anime_list = sorted(anime_list, key=lambda x: x["rating"], reverse=True)

        elif mode == "latest":
            anime_list = sorted(anime_list, key=self.date_value, reverse=True)

        elif mode == "az":
            anime_list = sorted(anime_list, key=lambda x: x["title"].lower())

        self.show_list(self.animeRankingList, anime_list)

    def date_value(self, anime):
        date = QDate.fromString(anime["release_date"], DATE_FORMAT)

        if date.isValid():
            return date.toJulianDay()

        return 0
