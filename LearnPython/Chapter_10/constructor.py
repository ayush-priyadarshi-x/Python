class Employee: 

    language : "python"
    salary : 10
    def __init__(self,name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        print(self.name, self.language, self.salary)
        print("This is a constructor. ")

Ayush = Employee("Ayush", "JavaScript", 120000 )

