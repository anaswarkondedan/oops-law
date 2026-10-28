class password:
    def __init__(self,password):
        self.password=password

    def change_password(self):
     old= input("enter the existing password :")

     if old==self.password:
        new=input("enter the new password :")
        print("password is coorect:")
        self.password=new
        print("password can changed :")
     else:
        print("password is wrong")

p=password("123456")
p.change_password()

                
            
        
        