class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.s=(self.a+self.b+self.c)/2

class TriangleArea(Triangle):
    
    def area(self):
        return((self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**(0.5))  


o2=TriangleArea(10,10,10)
print(o2.area()) 
