words = {
    "madad": "Help", 
    "kursi": "Chair", 
    "billi": "Cat", 
}

word = input("Enter word you want to know ")

print(words[word])
print(words.get(word, "No translation available"))