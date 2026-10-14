# class emplooy:
#     def __init__(self,name,id,salary):
#         self.name=name
#         self.id=id
#         self.salary=salary
# emplooy1=emplooy("biju",30131,30000)
# print("name:",emplooy1.name)
# print("id:",emplooy1.id)
# print("salary",emplooy1.salary)   

class emplooy:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
            print("emplooy name",self.name)
            print("emplooy id",self.id)
            print("emplooy",self.salary)
    name=(input("enter the persons name:"))
    emplooy=int(input("enter the id: "))
    emplooy=int(input("enter the salary: "))


# print("name:",e.name)
# print("id:",e.id)
# print("salary",e.salary)   