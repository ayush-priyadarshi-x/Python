f = open("this.txt", "r")
content = f.read()

if  content : 
    w = open("this_copy.txt", "w")
    w.write(content)