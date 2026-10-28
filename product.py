class product:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price
    def total_price(self):
         total=self.price* self.quantity
         print(self.name,"name:")
         print(self.price,"price:")
         print(self.quantity,"quantity:")
         
p1=product("jam",2000,3)
p1.total_price()