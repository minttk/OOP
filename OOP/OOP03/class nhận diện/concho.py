class concho:
    def __init__(self,ten,mausac,giong,camxuc):
        self.ten=ten
        self.mausac=mausac
        self.giong=giong
        self.camxuc=camxuc
    def sua(self):
        print(self.ten,"đang sủa")
    def vay_duoi(self):
        print(self.ten,"đang vấy đuôi")
    def an(self):
        print(self.ten,"đang ăn")
    def chay(self):
        print(self.ten,"đang chạy")
    def __str__(self):
        return (f"Tên:{self.ten:10}|Giống chó:{self.giong:8}|"
              f"Màu sắc:{self.mausac:10}|cảm xúc:{self.camxuc:8}")
cho1=concho("mixi","vang","poodle","vui")
print(cho1),cho1.sua(),cho1.vay_duoi(),cho1.an(),cho1.chay()