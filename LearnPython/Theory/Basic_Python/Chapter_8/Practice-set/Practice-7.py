def multiTable(n): 
    newTable = """"""
    for i in range(1, 11): 
        newTable += f"{(f"{n} X {i} = {n*i}")} \n"
    return newTable
    
print(multiTable(2))
