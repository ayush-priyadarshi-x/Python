from functools import reduce
list = [1, 2, 23, 45, 15, 85]

def greater(a,b): 
    if a>b: 
        return a
    return b

print(reduce(greater, list))