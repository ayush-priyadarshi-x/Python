class Employee:
    language = "Py"
    salary = 120000

# Create an instance (object) of the Employee class
harry = Employee()

# Access the attributes via the instance
print(harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan"
rohan.language = "JS"
rohan.salary = 130000
print(rohan.name, rohan.language, rohan.salary)