from abc import ABC, abstractmethod
class TuoiKhongHopLe(Exception):
    def __init__(self, tuoi):
        self.tuoi = tuoi
        super().__init__(f"Tuổi {tuoi} không hợp lệ (18–65)")
class BacKhongHopLe(Exception):
    def __init__(self, bac):
        self.bac = bac
        super().__init__(f"Bậc {bac} không hợp lệ (1–10)")
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten    = ho_ten
        self.tuoi = tuoi         # Gọi setter → validate
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi   = dia_chi
    @property
    def ho_ten(self):    return self.__ho_ten
    @property
    def gioi_tinh(self): return self.__gioi_tinh
    @property
    def dia_chi(self):   return self.__dia_chi
    @property
    def tuoi(self):
        return self.__tuoi
    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(value)
        self.__tuoi = value
    @abstractmethod
    def mo_ta(self):
        pass
    def __str__(self):
        return (f"{self.__ho_ten} | {self.__tuoi} tuổi"
                f" | {self.__gioi_tinh} | {self.__dia_chi}"
                f" | {self.mo_ta()}")
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__ho_ten}', {self.__tuoi})"
    def __eq__(self, other):
        if not isinstance(other, CanBo): return NotImplemented
        return self.__ho_ten == other.__ho_ten and self.__tuoi == other.__tuoi
    def __lt__(self, other):
        return self.__ho_ten < other.__ho_ten
    def __hash__(self):
        return hash((self.__ho_ten, self.__tuoi))
class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac          
    @property
    def bac(self): return self.__bac
    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(value)
        self.__bac = value
    def mo_ta(self):           
        return f"Công nhân bậc {self.__bac}"
class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh_dt = nganh_dt
    def mo_ta(self):
        return f"Kỹ sư ngành {self.__nganh_dt}"
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec
    def mo_ta(self):
        return f"Nhân viên — {self.__cong_viec}"
ds = [CongNhan("Tạ Đức Minh", 18, "Nam", "Hà Nội gốc", 5),
      KySu("Tần Đặng Quang", 19, "Nam", "Lào Cai", "CNTT"),
      NhanVien("Trần Bảo Khanh", 18, "Nữ", "Đà Nẵng", "Kế toán")]
print("── Đa hình: 1 vòng lặp, 3 loại CB ──")
for cb in ds:
    print(cb)
print("\n── Sắp xếp theo tên (A→Z) ──")
for cb in sorted(ds):
    print(f"  {cb.ho_ten}")
print("\n── Validation ──")
try:
    CongNhan("X", 15, "Nam", "HN", 5)
except TuoiKhongHopLe as e:
    print(f"  {e}")
try:
    CongNhan("Y", 25, "Nữ", "HN", 15)
except BacKhongHopLe as e:
    print(f"  {e}")
print("\n── Lưu file ──")
with open("canbo.txt", "w", encoding="utf-8") as f:
    for cb in ds:
        f.write(str(cb) + "\n")
print(f"  Đã lưu {len(ds)} cán bộ")
