class AnimeItem:
    def __init__ (self, anime_id, title, release_date, image=None, rating=None, link=None):
        self.id = anime_id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating = float(rating) if rating else 0
        self.link = link
    def update (self, new_data:dict):
        for attribute, value in new_data.items():
            if value:
                setattr(self, attribute, value)

## Khởi tạo danh sách đối tượng
# Tạo đối tượng
anime1 = AnimeItem(1, "Jujutsu no Kaisen", "01/01/2022")
anime2 = AnimeItem(2, "Kimetsu no Yaiba", "01/05/2022")
anime3 = AnimeItem(3, "Attack on Titan", "05/05/2019")

# Khởi tạo danh sách đối tượng
animes = [anime1, anime2, anime3]


# Duyệt danh sách đối tượng
print("__________________")
print("DUYET DANH SACH")
for anime in animes:
    print(anime.title)
print("__________________")


# Thêm đối tượng
print("THEM DOI TUONG MOI")
anime4 = AnimeItem(4, "One Piece", "01/01/1999")
animes.append(anime4)
for anime in animes:
    print(anime.title)
print("__________________")


# Xoá đối tượng
print("XOA DOI TUONG CU THE")
remove_title = "Attack on Titan"
for anime in animes:
    if anime.title == remove_title:
        animes.remove(anime)
for anime in animes:
    print(anime.title)
print("__________________")

# Cập nhập đối tượng
print("CAP NHAP DOI TUONG CU THE")
new_data = {
    "title": "Jujutsu no Kaisen 2",
    "release_date": "Unknown"
}
anime1.update(new_data)
print(anime1.title)
print(anime1.release_date)