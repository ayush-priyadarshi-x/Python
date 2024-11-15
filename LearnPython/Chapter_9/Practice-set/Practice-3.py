def generateTable(): 
    table = """"""
    for j in range(1, 21): 
        for i in range(1, 11): 
          table += f"""{j} X {i} = {j*i}  \n"""
        table += "\n\n\n"
        
    return table

with open("multiplicationTable.txt", "w") as f: 
    f.seek(0)
    generatedTable =  generateTable()
    print(generatedTable)
    f.write(generatedTable)