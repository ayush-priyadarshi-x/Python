class Employee: 
    a=1
    @classmethod
    def show(cls): 
        print(f"The value of a is {cls.a}")

a = Employee()
a.a = 23
a.show()