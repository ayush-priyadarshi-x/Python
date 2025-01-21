import math
class Calculator: 
    def __init__(self, number):
        self.number = number if number>0 else 0 

    def square(self): 
       sqr = self.number*self.number
       return sqr
    def cube(self): 
      cube = self.number*self.number*self.number
      return cube
    def squareRoot(self): 
        return math.sqrt(self.number)
        


myNum = Calculator(12)
print(f"The square : {myNum.square()} \n Cube : {myNum.cube()} \n Square root : {myNum.squareRoot()}")