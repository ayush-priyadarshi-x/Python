class Employee:
    # Class Attributes
    language = "Python"  # Class attribute for language
    salary = 120000      # Class attribute for salary
     
    def getInfo(self): 
        # Instance method that prints the employee's info
        print(f"The language is {self.language} and Salary is : {self.salary}")
    
    def greet(self):  # self must be there. 
        print("Good morning")

# Create an instance of Employee
harry = Employee()

# Call the method to print information
harry.getInfo()  # Same : Employee.getInfo(harry)
