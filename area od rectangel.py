class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length  * self.width
    
length=float(input("enter the length: "))
width=float(input("enter the width: "))

r1= rectangle(length, width)
print("area of rectangle:",r1.calculate_area())


