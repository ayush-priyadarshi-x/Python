def resetFile(fileName): 
    with open(fileName, "w") as f: 
        f.seek(0)
        f.write("")

resetFile("donkey.txt")