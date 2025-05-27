f = open("berserk.png", "rb")
 
f1 = open("anotherBerserk.png", 'wb')

for i in f: 
    f1.write(i)