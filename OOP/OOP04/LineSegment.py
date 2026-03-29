import math
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self, x):
        self.__x = x
    def set_y(self, y):
        self.__y = y
    def __str__(self):
        return f"({self.__x}, {self.__y})"
class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2:
            self.__d1 = args[0]
            self.__d2 = args[1]
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1:
            s = args[0]
            self.__d1 = Point(s.getD1().get_x(), s.getD1().get_y())
            self.__d2 = Point(s.getD2().get_x(), s.getD2().get_y())
        else:
            print("Lỗi tham số")
    def getD1(self):
        return self.__d1
    def getD2(self):
        return self.__d2
    def setD1(self, p):
        self.__d1 = p
    def setD2(self, p):
        self.__d2 = p
    def length(self):
        dx = self.__d1.get_x() - self.__d2.get_x()
        dy = self.__d1.get_y() - self.__d2.get_y()
        return math.sqrt(dx**2 + dy**2)
    def print(self):
        print(f"{self.__d1} -> {self.__d2}"
if __name__ == "__main__":
    a = LineSegment()
    print("a:", end=" "); a.print()
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    b = LineSegment(p1, p2)
    print("b:", end=" "); b.print()
    c = LineSegment(1, 2, 5, 6)
    print("c:", end=" "); c.print()
    d = LineSegment(c)
    print("d:", end=" "); d.print()
    print("Độ dài c =", c.length())
