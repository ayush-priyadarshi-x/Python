givenListOfNameFromDB = ["Ayush"]  # Some information which we will get later from the Database. 

enteredName = input("Enter your name : ")

if(enteredName in givenListOfNameFromDB): 
    print("The username is not unique. ")
else: 
    print("The username is unique")

