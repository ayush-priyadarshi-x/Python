l = ["Harry", "Rohan", "Subham", "an"]

def removeListItem(listI, word): 
    for item in listI: 
        l.remove(word)
        return l 
    
print(removeListItem(l, "an"))