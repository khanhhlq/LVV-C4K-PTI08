# Thêm file data_io từ folder data
from data import data_io
# Thêm thư viện datattime
from datetime import datetime
# Thêm thư viện operator
import operator

class AnimeItem:
    def __init__ (self, anime_id, title, release_date, image=None, rating=None, link=None):
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating) if rating else 0
        self.link = link
    
    def __repr__(self):
        return f"AnimeItem(id={self.id}, title='{self.title}', rating={self.rating})"
    
    def update(self, new_data:dict):
        for attribute, value in new_data.items():
            if value:
                setattr(self, attribute, value)

class AnimeDatabase:
    def __init__(self):
        self.anime_item_list = list()
        self.anime_dict_data = data_io.load_json_data()
        self.load_data()
        
    def load_data(self):
        for anime_dict in self.anime_dict_data:
            anime = AnimeItem(
                anime_id = anime_dict["id"],
                title = anime_dict["title"],
                release_date = anime_dict["release_date"],
                image = anime_dict["image"],
                link = anime_dict["link"]
            )
            self.anime_item_list.append(anime)
    
    # Hàm chuyển đổi data vào json
    def items_to_data(self):
        json_data = list()
        for anime in self.anime_item_list:
            json_data.append(anime.__dict__)
        return json_data
        
    def get_first_item_by_title(self, anime_title):
        for anime_item in self.anime_item_list:
            # Tìm thấy
            if anime_item.title == anime_title:
                return anime_item
        # Không tìm thấy
        return False
    
    def add_item(self, anime_dict):
        anime_dict["id"] = len(self.anime_item_list)
        new_item = AnimeItem(
            anime_id = anime_dict["id"],
            title = anime_dict["title"],
            release_date = anime_dict["release_date"],
            image = anime_dict["image"],
            rating = anime_dict["rating"],
            link = anime_dict["link"]
        )
        self.anime_item_list.append(new_item)
        
        self.anime_dict_data.append(anime_dict)
        data_io.write_json_data(self.anime_dict_data)
        
    def edit_item(self, edit_title, new_dict):
        matched = self.get_first_item_by_title(edit_title)
        if matched:
            matched.update(new_dict)
            self.anime_dict_data = self.items_to_data()
            data_io.write_json_data(self.anime_dict_data)
            
    
    def delete_item(self, delete_title):
        matched = self.get_first_item_by_title(delete_title)
        if matched:
            self.anime_item_list.remove(matched)
    
    def search_by_title(self, search_title) -> list[AnimeItem]:
        matched_items = []
        for anime_item in self.anime_item_list:
            if search_title.lower() in anime_item.title.lower():
                matched_items.append(anime_item)
        return matched_items

    def sort_item_by_rating(self, top=None):
        self.anime_item_list = sorted(
            self.anime_item_list,
            key = operator.attrgetter('rating'),
            reverse=True
        )
        if top:
            return self.anime_item_list[:top]
        
    def sort_item_by_title(self, top=None):
        self.anime_item_list = sorted(
            self.anime_item_list,
            key = operator.attrgetter('title'),
        )
        if top:
            return self.anime_item_list[:top]
        
    def sort_item_by_date(self, top=None):
        self.anime_item_list = sorted(
            self.anime_item_list,
            key = lambda x:
                format_date(x.release_date),
            reverse=True
        )
        if top:
            return self.anime_item_list[:top]
        
def format_date(date_text):
    return datetime.strptime(date_text, '%d/%m/%Y')

# TEST THỬ LOAD DATA TỪ JSON
anime_db = AnimeDatabase()

print("DANH SACH ANIME")
print(anime_db.anime_item_list)

# TEST CHỨC NĂNG THÊM ITEMS
anime_db.add_item(
    {
    "id": 19,
    "title": "Blue Lock",
    "release_date": "09/10/2022",
    "image": None,
    "rating": 8.3,
    "link": None
    }
)
