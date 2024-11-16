class Employee:
    # Class attributes
    language = "Python"
    salary = 1200000

# Create an instance of Employee
harry = Employee()

# Override the class attribute with an instance attribute
harry.language = "JavaScript"

# Print the instance's language and salary
print(harry.language, harry.salary)
