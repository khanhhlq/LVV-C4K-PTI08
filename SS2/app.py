## Hãy viết lớp mô tả hình chữ nhật và phương thức
# Tính chu vi hình chữ nhật
# Tính diện tích hình chữ nhật

class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def tinh_chu_vi(self):
        return (self.chieu_rong + self.chieu_dai)*2
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
hcn = HinhChuNhat(4, 5)
print(hcn.tinh_chu_vi())
print(hcn.tinh_dien_tich())


