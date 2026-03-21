import math
class point:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
class circle:
    def __init__(self,center:point,radius:float):
        self.center=center
        self.radius=radius
    def point_in_circle(self,other):
        d=math.sqrt((self.center.x-other.x)**2+(self.center.y-other.y)**2)
        return  d <= self.radius
class Rectangle:
    def __init__(self,x:int,y:int,width:int,height:int):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def point_corners(self):
        return [point(self.x,self.y)
                ,point(self.x+self.width,self.y)
                ,point(self.x,self.y+self.height)
                ,point(self.x+self.width,self.y+self.height)]
    def rect_in_circle(self, c: circle):
        for p in self.point_corners():
            if not c.point_in_circle(p):
                return False
        return True
    def overlap_circle(self, c):
        for p in self.point_corners():
            if c.point_in_circle(p):
                return True
        return False
c = circle(point(0, 0), 5)
K=point(2,1)
print(c.point_in_circle(K))
rect1 = Rectangle(1, 1, 2, 2)
print(rect1.rect_in_circle(c)) 
rect2 = Rectangle(10, 10, 2, 2)
print(rect2.overlap_circle(c))  


        
        