import math
class Circle:
    def __init__(self):
        pass
    def radius(self,diameter):
        self.radius_of_circle=diameter/2
        print("Radius:",self.radius_of_circle)
    def area(self,r):
        self.area_of_circle=math.pi*r**2
        print(self.area_of_circle)
    def circumference(self,r):
        self.circumference_of_circle=2*math.pi*r
        print(self.circumference_of_circle)
circle=Circle()
diameter=float(input("Enter a diameter"))
r=diameter/2

circle.radius(diameter)
circle.area(r)
circle.circumference(r)

