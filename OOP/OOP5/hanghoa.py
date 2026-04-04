class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._gia = gia
    def thong_tin_chung(self):
        return (f"Mã: {self._ma_hang} | "
                f"Tên: {self._ten_hang} | "
                f"NSX: {self._nha_sx} | "
                f"Giá: {self._gia:,.0f} VNĐ")
    def __str__(self):
        return self.thong_tin_chung()
class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia,
                 bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._bao_hanh = bao_hanh
        self._dien_ap = dien_ap
        self._cong_suat = cong_suat
    def __str__(self):
        return (f"[ĐIỆN MÁY] {super().__str__()} | "
                f"BH: {self._bao_hanh} tháng | "
                f"{self._dien_ap}V | {self._cong_suat}W")
class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._nguyen_lieu = nguyen_lieu
    def __str__(self):
        return (f"[SÀNH SỨ] {super().__str__()} | "
                f"Nguyên liệu: {self._nguyen_lieu}")
class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia,
                 ngay_sx, han_su_dung):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._ngay_sx = ngay_sx
        self._han_su_dung = han_su_dung
    def __str__(self):
        return (f"[THỰC PHẨM] {super().__str__()} | "
                f"NSX: {self._ngay_sx} | HSD: {self._han_su_dung}")
ds = [
    HangDienMay("DM01", "Máy giặt", "LG", 8000000, 24, 220, 500),
    HangSanhSu("SS01", "Bình gốm", "Bát Tràng", 300000, "Gốm"),
    HangThucPham("TP01", "Bánh", "Kinh Đô", 20000, "01/04/2026", "01/06/2026")
]
for hang in ds:
    print(hang)
