import math
class point:
    def __init__(self,x: int,y: int):
        self.x=x
        self.y=y
    def hienthi(self):
        print(f"Điểm({self.x},{self.y})")
    def doixung(self):
        return point(-self.x,-self.y)
    def khoangcachdenO(self):
        return math.sqrt(self.x**2+self.y**2)
    def khoangcach2diem(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
A=point(3,4)
xb=int(input())
yb=int(input())
B=point(xb,yb)
print("điểm B: "); B.hienthi()
C=B.doixung()
print("điểm C:");C.hienthi()
print(f"Khoảng cách từ B đến O là :{B.khoangcachdenO():.2f}")
print(f"Khoảng cách từ A đến B là: {A.khoangcach2diem(B):.2f}")