import json
from pathlib import Path


class AnimeDatabase:
    """
    Class quản lý dữ liệu anime bằng file JSON.
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.anime_dict_data = []

    def load_data(self):
        if not self.file_path.exists():
            self.anime_dict_data = []
            self.save_data()
            return

        with open(self.file_path, "r", encoding="utf-8") as file:
            self.anime_dict_data = json.load(file)

    def save_data(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.anime_dict_data, file, ensure_ascii=False, indent=4)

    def get_all_items(self):
        return self.anime_dict_data

    def get_first_item_by_title(self, title):
        for anime in self.anime_dict_data:
            if anime["title"] == title:
                return anime

        return None

    def add_item(self, anime):
        anime["id"] = self.next_id()
        self.anime_dict_data.append(anime)
        self.save_data()

    def edit_item(self, old_title, new_data):
        for index, anime in enumerate(self.anime_dict_data):
            if anime["title"] == old_title:
                new_data["id"] = anime["id"]
                self.anime_dict_data[index] = new_data
                self.save_data()
                return

    def delete_item(self, title):
        self.anime_dict_data = [
            anime for anime in self.anime_dict_data
            if anime["title"] != title
        ]

        self.save_data()

    def search_by_title(self, keyword):
        keyword = keyword.lower().strip()

        return [
            anime for anime in self.anime_dict_data
            if keyword in anime["title"].lower()
        ]

    def next_id(self):
        if not self.anime_dict_data:
            return 1

        return max(anime["id"] for anime in self.anime_dict_data) + 1
