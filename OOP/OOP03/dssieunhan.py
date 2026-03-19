class sieunhan:
    def __init__(self,ten="",vukhi="",mausac="",dongu=0):
        self.ten=ten
        self.vukhi=vukhi
        self.mausac=mausac
        self.dongu=dongu
    def __str__(self):
        return(f"Tên:{self.ten:10}|Vũ khí{self.vukhi:8}|"
              f"Màu sác:{self.mausac:10}|Độ ngu{self.dongu:8}")
danhsach=[]
print("     DANH SÁCH QUẢN LÝ SIÊU NHÂN     ")
print("     (Nhấn Enter để kết thúc)\n      ")
while True:
    ten = input("Tên siêu nhân: ")
    if ten == "":
        break
    vukhi  = input("Vũ khí: ")
    mausac = input("Màu sắc: ")
    dongu = int(input("Độ ngu (1-100): "))
    danhsach.append(sieunhan(ten, vukhi, mausac, dongu))
    print(f"  → Đã thêm {ten}!\n")

print(f"\n=== DANH SÁCH {len(danhsach)} SIÊU NHÂN ===")
for i, sn in enumerate(danhsach, 1):
    print(f"{i}.", sn)

    