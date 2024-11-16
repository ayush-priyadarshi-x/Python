with open("this.txt", "r") as f: 
    content1 = f.read()

with open("this_copy.txt", "r") as w: 
    content2 = w.read()

if content1.upper() == content2.upper(): 
    print("The content of this.txt and this_copy.txt matches. ")
else: 
    print("The content of this.txt and this_copy.txt doesn't match. ")
