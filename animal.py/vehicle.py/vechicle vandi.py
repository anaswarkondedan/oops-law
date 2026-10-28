class vehicle:
    def __init__(self,brand,model,colour):
        self.brand=brand
        self.model=model
        self.colour=colour

    def display(self):
        print(self.brand,"brand :")
        print(self.model,"model :")
        print(self.colour,"colour :")

class Car(vehicle):

    def __init__(self, brand, model, color, doors):
        super().__init__(brand, model, color)
        self.doors = doors

def car_details(self):
        self.display()
        print("Number of doors:", self.doors)

class Bike(vehicle):
    def __init__(self, brand, model, color, engine_cc):
        super().__init__(brand, model, color)
        self.engine_cc = engine_cc

    def bike_details(self):
        self.display()
        print("Engine capacity:", self.engine_cc, "cc")


car1 = Car("Toyota", "Fortuner", "Black", 4)
bike1 = Bike("Yamaha", "R15", "Blue", 155)

print("Car Details")
car1.car_details()

print("\nBike Details")
bike1.bike_details()

        