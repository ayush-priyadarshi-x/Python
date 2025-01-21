f = open("file.txt")
print(f.read())

f.close()

# The same can be done using with 

with open("file.txt" ) as f: 
    print(f.read())