class Employee: 
    def __init__(self):
        print("Constructor of Employee ")

    a = 1
class Programmar(Employee): 
    def __init__(self):
        super().__init__()
        print("Constructor of Programmar ")

    b = 2
class Manager(Programmar): 
    def __init__(self):
        super().__init__()
        print("Constructor of Manager ")

    c = 3


a = Manager()