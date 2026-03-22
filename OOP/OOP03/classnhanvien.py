class NhanVien:
    def __init__(self, tennhanvien: str, luongcoban: float, heSoLuong: float, LUONGMAX: float):
        self.tennhanvien = tennhanvien
        self.luongcoban = luongcoban
        self.heSoLuong = heSoLuong
        self.LUONGMAX = LUONGMAX
    def get_tennhanvien(self):
        return self.tennhanvien
    def get_luongcoban(self):
        return self.luongcoban
    def get_heSoLuong(self):
        return self.heSoLuong
    def get_LUONGMAX(self):
        return self.LUONGMAX
    def set_tennhanvien(self, ten):
        if ten.strip() != "":
            self.tennhanvien = ten
    def set_luongcoban(self, luong):
        if luong > 0:
            self.luongcoban = luong
    def set_heSoLuong(self, heso):
        if heso > 0:
            self.heSoLuong = heso
    def set_LUONGMAX(self, max_luong):
        if max_luong > 0:
            self.LUONGMAX = max_luong
    def tinhluong(self):
        return self.luongcoban * self.heSoLuong
    def inTTin(self):
        print(self)
    def tangLuong(self, delta):
        luong_moi = self.tinhluong() + delta
        if luong_moi > self.LUONGMAX:
            print("Vượt quá LUONGMAX!")
            return False
        else:
            self.heSoLuong = luong_moi / self.luongcoban
            return True
    def __str__(self):
        return f"{self.tennhanvien} | LCB: {self.luongcoban} | HSL: {self.heSoLuong} | Lương: {self.tinhluong()}"
nv = NhanVien("An", 5000, 2, 15000)
nv.inTTin()
print("---- Tăng lương ----")
if nv.tangLuong(3000):
    print("Tăng lương thành công")
else:
    print("Tăng lương thất bại")
nv.inTTin()