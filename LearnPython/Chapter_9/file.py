"""
This is the text inside a program. We will now be reading a file. 
"""

f = open("file.txt", "r")
data = f.read()
print(data)
# print(f"The data fetched from the file.txt is : {data}")
f.close()