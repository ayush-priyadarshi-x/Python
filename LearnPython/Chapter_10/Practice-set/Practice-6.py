class Calculator:
    # Constructor using 'slf' instead of 'self'
    def __init__(slf, number):
        slf.number = number

    # Method to calculate square using 'slf'
    def square(slf):
        return slf.number * slf.number

    # Method to calculate cube using 'slf'
    def cube(slf):
        return slf.number * slf.number * slf.number

# Creating an object of Calculator class
myCalculator = Calculator(5)

# Calling the methods
print(f"Square of {myCalculator.number}: {myCalculator.square()}")
print(f"Cube of {myCalculator.number}: {myCalculator.cube()}")
