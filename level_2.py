class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist(x,y):
        return(x**2+y**2)**(1/2)

    def __add__(self,other):
        return(self.x + other.x, self.y + other.y)

print(Point.dist(2,3))
#print(Point.__add__(4,3))
p1 = Point(1,1)
p2 = Point(2,2)
p3 = p1+p2
print(p3)




