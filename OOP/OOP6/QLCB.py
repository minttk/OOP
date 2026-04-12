from abc import ABC, abstractmethod
class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        super().__init__(f"Tuổi {tuoi} không hợp lệ (18–65)")
class BacKhongHopLe(Exception):
    def __init__(self, bac):
        super().__init__(f"Bậc {bac} không hợp lệ (1–10)")
class CanBo(ABC):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi):
        self._ten = ten
        self.tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi
    @property
    def tuoi(self):
        return self._tuoi
    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(value)
        self._tuoi = value
    @abstractmethod
    def mo_ta(self):
        pass
    def __str__(self):
        return (f"{self._ten} | {self._tuoi} | {self._gioi_tinh}"
                f" | {self._dia_chi} | {self.mo_ta()}")
    def __lt__(self, other):
        return self._ten < other._ten
    def __eq__(self, other):
        return isinstance(other, CanBo) and self._ten == other._ten and self._tuoi == other._tuoi
    def __hash__(self):
        return hash((self._ten, self._tuoi))
class Worker(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
    @property
    def bac(self):
        return self._bac
    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(value)
        self._bac = value
    def mo_ta(self):
        return f"Công nhân bậc {self._bac}"
class Engineer(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, chuyen_nganh):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self._chuyen_nganh = chuyen_nganh
    def mo_ta(self):
        return f"Kỹ sư {self._chuyen_nganh}"
class Staff(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, vi_tri):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self._vi_tri = vi_tri
    def mo_ta(self):
        return f"Nhân viên {self._vi_tri}"
ds = [
    Worker("Nguyễn Văn An", 25, "Nam", "Hải Phòng", 3),
    Engineer("Lê Thị Mai", 30, "Nữ", "Hà Nội", "Phần mềm"),
    Staff("Phạm Minh Tuấn", 28, "Nam", "TP.HCM", "Hành chính")
]
print("── Danh sách cán bộ ──")
for cb in ds:
    print(cb)
print("\n── Sắp xếp theo tên ──")
for cb in sorted(ds):
    print(cb._ten)
print("\n── Test trùng ──")
cb_clone = Worker("Nguyễn Văn An", 25, "Nam", "Đà Nẵng", 5)
print("Trùng:", ds[0] == cb_clone)
print("\n── Test set ──")
print(len(ds), "→", len(set(ds)))
print("\n── Test lỗi ──")
try:
    Worker("Test", 10, "Nam", "HN", 3)
except TuoiKhongHopLe as e:
    print(e)
try:
    Worker("Test", 25, "Nam", "HN", 20)
except BacKhongHopLe as e:
    print(e)
print("\n── Lưu file ──")
with open("canbo.txt", "w", encoding="utf-8") as f:
    for cb in ds:
        f.write(str(cb) + "\n")
print("Đã lưu", len(ds), "cán bộ")
