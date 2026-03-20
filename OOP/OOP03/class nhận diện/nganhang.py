class taikhoan:
    def __init__(self,tentk,sotk,nganhang,sodu):
        self.tentk=tentk
        self.sotk=sotk
        self.nganhang=nganhang
        self.sodu=sodu
    def rut(self,sotien):
        if sotien<=self.sodu:
            self.sodu-=sotien
            print("rút thành công")
        else:
            print("số dư tài khoản không đủ")
    def gui(self,sotien):
        self.sodu+=sotien
        print("gửi thành công")
    def kiemtra(self):
        print("số dư:",self.sodu)
    def __str__(self):
        return (f"Tên tài khoản:{self.tentk:10}|số tài khoản:{self.sotk:8}|"
              f"ngân hành:{self.nganhang:10}|số dư:{self.sodu:,.0f} VNĐ")
tk=taikhoan("Nguyễn Thị A","000000001","MB BANK",20000000000)
print(tk)
print(f"{'MENU':^50}")
print("Hãy chon hành động")
print(f"{'1 rút tiền':12}|{'2 gửi tiền':12}|{'3 kiểm tra số dư':12}")
hd=input()
if hd=="1":
    tien=float(input("số tiền: "))
    tk.rut(tien)
elif hd=="2":
    tien=float(input("số tiền: "))
    tk.gui(tien)
elif hd=="3":
    tk.kiemtra()
else:
    print("lựa chọn không hợp lệ")
