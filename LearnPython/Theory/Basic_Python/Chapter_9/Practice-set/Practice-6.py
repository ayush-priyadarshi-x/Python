f= open("log.txt")
content = f.read()
if "python".upper() in content.upper(): 
   print("The text contains python. ")
else: 
   print("The text does not contain python. ")