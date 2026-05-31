class AnimeItem:
    def __init__(self, anime_id, title, release_date,
                 image=None, rating=None, link=None):
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image = image

        # Nếu không có rating thì mặc định bằng 0
        self.rating = float(rating) if rating else 0
        self.link = link

    def update(self, new_data: dict):
        # Chỉ khi nào thuộc tính có giá trị mới thì mới update
        for attribute, value in new_data.items():
            if value:
                setattr(self, attribute, value)

# Tạo các đối tượng anime
anime1 = AnimeItem(1, "Jujutsu no Kaisen", "01/01/2022")
anime2 = AnimeItem(2, "Kimetsu no Yaiba", "01/05/2022")
anime3 = AnimeItem(3, "Attack on Titan", "05/05/2019")

# Danh sách anime
animes = [anime1, anime2, anime3]

# Duyệt danh sách và in tên anime
print("Danh sach anime ban dau")
for anime in animes:
    print(anime.title)

# Thêm anime mới vào danh sách
anime4 = AnimeItem(4, "One Piece", "01/01/1999")
animes.append(anime4)

print("\nDanh sach anime sua khi them moi")
for anime in animes:
    print(anime.title)

# Ví dụ cập nhật thông tin anime
anime1.update({
    "rating": 9.5,
    "link": "https://example.com/jujutsu-kaisen"
})

print("\nThong tin anime sau khi cap nhat")
print("Ten:", anime1.title)
print("Ngay phat hanh: ", anime1.release_date)
print("Rating:", anime1.rating)
print("Link:", anime1.link)

# 31/05/2026

class AnimeList:
    def __init__(self):
        # Tạo danh danh sách chứa các dối tượng AnimeItem
        self.animes_item_list = list()
    def get_first_item_by_title(self, anime_title):
        # Trả về đối tượng AnimeItems có title là anime_title
        for i in self.animes_item_list:
            if i.title == anime_title:
                return i
        return False
    def add_item(self, anime_dict):
        anime_dict["id"] = len(self.animes_item_list)
        new_item = AnimeItem(anime_id = anime_dict["id"],
                             title = anime_dict["title"],
                             release_date = anime_dict["release_date"],
                             image = anime_dict["image"],
                             rating = anime_dict["rating"],
                             link = anime_dict["link"])
        self.animes_item_list.append(new_item)
    def edit_item(self, edit_title, new_dict):
        # Tìm đối tượng
        matched = self.get_first_item_by_title(edit_title)
        if matched:
            matched.update(new_dict)
    def delete_item(self, delete_title):
        # Phương thức xoá đối tượng AnimeItem có title delete_title
        matched = self.get_first_item_by_title(delete_title)
        if matched:
            self.animes_item_list.remove(matched)
    def search_by_title(self, search_title) -> list[AnimeItems]:
        # Phương thức tìm kiếm tất cả các đối tượng AnimeItem có title là search_title
        matched_items = []
        for i in self.animes_item_list:
            if search_title in i.title.lower():
                matched_items.append(i)
        return matched_items
    def sort_items_by_rating(self, top=None):
        # Phương thức sắp xếp theo rating
        self.animes_item_list = sorted(self.animes_item_list,
                                       key = operator.attrgetter("rating"),
                                       reverse = True)
        if top:
            return self.animes_item_list[top]
    def sort_items_by_title(self, top=None):
        # Phương thức sắp xếp theo title
        self.animes_item_list = sorted(self.animes_item_list,
                                       key = operator.attrgetter("title"))
        if top:
            return self.animes_item_list[top]
    def sort_items_by_date(self, top=None):
        # Phương thức sắp xếp theo ngày phát hành
        self.animes_item_list = sorted(self.animes_item_list,
                                       key = lambda x: format_date(x.release_date))
        if top:
            return self.animes_item_list[top]
    def format_date(date_text):
        return datetime.strptime(date_text, '%b %Y')

anime_list = AnimeList()
anime_list.add_item({
    "title": "Doraemon",
    "release_date": "31/05/2026",
    "image": "https://example.com/doraemon.jpg",
    "rating": 9.0,
    "link": "https://example.com/doraemon"
})

anime_list.add_item({
    "title": "One Piece",   
    "release_date": "20/10/1999",
    "image": "https://example.com/one-piece.jpg",
    "rating": 9.8,
    "link": "https://example.com/one-piece"
})

anime_list.add_item({
    "title": "Naruto",  
    "release_date": "15/09/2002",
    "image": "https://example.com/naruto.jpg",
    "rating": 9.2,
    "link": "https://example.com/naruto"
})

print("Danh sach anime sau khi them moi:")
for anime in anime_list.animes_item_list:
    print(anime.title)


anime_list.edit_item("Doraemon", {
    "rating": 9.5,
    "link": "https://example.com/doraemon-updated"
})
print(anime_list.animes_item_list[0].rating)

anime_list.delete_item("Doraemon")
print(anime_list.animes_item_list)

anime_list.sort_items_by_rating()
print("Anime co rating cao nhat:", anime_list.animes_item_list[0].title)

anime_list.sort_items_by_title()
print("Anime co title dau tien:", anime_list.animes_item_list[0].title)

anime_list.sort_items_by_date()
print("Anime co ngay phat hanh som nhat:", anime_list.animes_item_list[0].title)

anime_list.search_by_title("One Piece")
print("Anime tim duoc:", anime_list.search_by_title("One Piece")[0].title)