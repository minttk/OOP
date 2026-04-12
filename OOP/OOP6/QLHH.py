from abc import ABC, abstractmethod
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        super().__init__(f"Giá '{gia}' không hợp lệ (>= 0)")
class HangHoa(ABC):
    def __init__(self, ma, ten, nsx, gia):
        self._ma = ma
        self._ten = ten
        self._nsx = nsx
        self.gia = gia
    @property
    def gia(self):
        return self._gia
    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value)
        self._gia = value
    @abstractmethod
    def loai(self):
        pass
    def __str__(self):
        return f"[{self.loai()}] {self._ma} | {self._ten} | {self._nsx} | {self._gia:,.0f}đ"
    def __lt__(self, other):
        return self._gia < other._gia
    def __eq__(self, other):
        return isinstance(other, HangHoa) and self._ma == other._ma
    def __hash__(self):
        return hash(self._ma)
class DienTu(HangHoa):
    def __init__(self, ma, ten, nsx, gia, bao_hanh):
        super().__init__(ma, ten, nsx, gia)
        self._bao_hanh = bao_hanh
    def loai(self):
        return "Điện tử"
    def __str__(self):
        return super().__str__() + f" | BH: {self._bao_hanh} tháng"
class GomSu(HangHoa):
    def __init__(self, ma, ten, nsx, gia, chat_lieu):
        super().__init__(ma, ten, nsx, gia)
        self._chat_lieu = chat_lieu
    def loai(self):
        return "Gốm sứ"
    def __str__(self):
        return super().__str__() + f" | CL: {self._chat_lieu}"
class DoAn(HangHoa):
    def __init__(self, ma, ten, nsx, gia, hsd):
        super().__init__(ma, ten, nsx, gia)
        self._hsd = hsd
    def loai(self):
        return "Đồ ăn"
    def __str__(self):
        return super().__str__() + f" | HSD: {self._hsd}"
sp1 = DienTu("E01", "Tai nghe Bluetooth", "Sony", 2_500_000, 12)
sp2 = GomSu("G01", "Ly uống trà", "Bát Tràng", 150_000, "Sứ trắng")
sp3 = DoAn("F01", "Bánh mì", "ABC Bakery", 20_000, "2026-04-15")
ds = [sp1, sp2, sp3]
print("── Danh sách ──")
for sp in ds:
    print(sp)
print("\n── Sắp xếp giá ──")
for sp in sorted(ds):
    print(sp)
print("\n── Test trùng ──")
sp1_clone = DienTu("E01", "Loa", "JBL", 3_000_000, 6)
print("Trùng:", sp1 == sp1_clone)
print("\n── Test set ──")
print(len(ds), "→", len(set(ds)))
print("\n── Test lỗi ──")
try:
    sp_loi = DienTu("E99", "Test", "X", -100, 6)
except GiaKhongHopLe as e:
    print(e)
