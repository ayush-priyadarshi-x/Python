def readPoem(): 
    with open("poems.txt") as f: 
        poem = f.read()
        if(not("Twinkle" in poem )): 
         return print("The given poem does not contain twinkle twinkle little star. ") 
        print("The given poem contains twinkle twinkle little star. ")

readPoem()