import math

class circle:
    def __init__(self,radius):
        self.radius=radius
        
    def calculate_area(self):
            return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
         return 2* math.pi* self.radius

radious= float(input("enter radius: "))
c1= circle (radious)

print("area of circle",round(c1.calculate_area()))
print("circumfernce of circle",round(c1.calculate_circumference() ))
             


        