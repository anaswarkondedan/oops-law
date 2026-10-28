class mark:
    def __init__(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
    def total_mark(self):
        total=self.mark1+ self.mark2+self.mark3
        print(total,"total")
        return total
      
    def average_mark (self):
        average= self.total_mark() /3
        print(average,"average")

        if average>=90:
           print ("A")
        elif average>=80:
            print("b")
        elif average>=70:
            print("c")
        else:
            print("failed") 
        
         

m1=mark(100,99,77)
m1.total_mark()
m1.average_mark()



