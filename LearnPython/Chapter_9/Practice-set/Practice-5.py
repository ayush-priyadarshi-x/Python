vulgurWords = ["stupid","idiot","jerk","dumb","loser",]
with open("vulgur.txt", "r+") as f: 
    content = f.read()
    for vulgurWord in vulgurWords: 
        if vulgurWord.upper() in content.upper(): 
            f.seek(0)
            content = content.replace(vulgurWord, "****")        
            f.write(content)