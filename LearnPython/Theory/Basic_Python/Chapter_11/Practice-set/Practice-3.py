class Employee: 
    def __init__(self, name, salary):
        self.name  = name
        self.salary  = salary
    def Increment(self, newSalary): 
        if self.salary > newSalary : 
            print("The given new salary is less than the previous one. ")
            return
        
        print(f" Old salary : {self.salary} \n New salary : {newSalary}")
        self.salary += newSalary 

    
Ayush = Employee("Ayush ", 100000)
Ayush.Increment(100000000000000)