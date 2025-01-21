x = 10  # Global variable

def modify_global():
    global x  # Declare x as global
    x = 20  # Modify the global variable

modify_global()
print(x)  # Output: 20
