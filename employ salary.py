class salary:
    def __init__(self,name,salary,):
        self.name=name
        self.salary=salary

    def increase_salary(self,percentage ):
        increase=self.salary* percentage/100
        self.salary=self.salary+ increase

        print("employ name",self.name)
        print("employ salary",self.salary)

e=salary("anaswar", 450000)
e.increase_salary(10)

        