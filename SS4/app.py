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

class AnimeList:
    def __init__(self):
        self.anime_item_list = list()
        
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
        
    def edit_item(self, edit_title, new_dict):
        matched = self.get_first_item_by_title(edit_title)
        if matched:
            matched.update(new_dict)
    
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

# TEST THỬ CÁC CHỨC NĂNG
anime_list = AnimeList()

# TEST HÀM ADD_ITEM
anime_list.add_item(
    {
        "id": 0,
        "title": "Jujutsu no Kaisen",
        "release_date": "01/01/2022",
        "image": None,
        "rating": 8,
        "link": None
    }
)

anime_list.add_item(
    {
        "id": 1,
        "title": "Kimetsu no Yaiba",
        "release_date": "05/06/2019",
        "image": None,
        "rating": 9,
        "link": None
    }
)

anime_list.add_item(
    {
        "id": 2,
        "title": "Attack on Titan",
        "release_date": "08/04/2018",
        "image": None,
        "rating": 10,
        "link": None
    }
)
print("SAU KHI ADD")
print(anime_list.anime_item_list)

# TEST HÀM EDIT_ITEM
anime_list.edit_item(
    "Jujutsu no Kaisen",
    {
        "title": "Jujutsu no Kaisen 2"
    }
)
print("SAU KHI EDIT")
print(anime_list.anime_item_list)

# TEST HÀM DELETE_ITEM
anime_list.delete_item("Jujutsu no Kaisen")
print("SAU KHI DELETE")
print(anime_list.anime_item_list)

# TEST HÀM SEARCH
print("TIM 1 BO PHIM DUA VAO TEN")
print(anime_list.search_by_title("Attack on Titan"))

# TEST HÀM SẮP XẾP PHIM THEO RATING
print("PHIM TOP 1")
print(anime_list.sort_item_by_rating(1))
