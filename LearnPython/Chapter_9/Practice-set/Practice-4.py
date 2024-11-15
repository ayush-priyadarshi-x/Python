with open("donkey.txt", "r+") as f: 
    content = f.read()
    if "donkey".upper() in content.upper(): 
        f.seek(0)
        content = content.replace("donkey", "monkey")
        f.write(content)
        f.truncate()  # Clears the rest of the file after the new content
        print(content)
    else: 
        print("The file does not contain the word 'donkey'.")
