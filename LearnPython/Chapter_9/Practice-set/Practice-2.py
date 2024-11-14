import random
def game(): 
    score = int(input("Enter you number. "))
    score *= random.randint(1, 100)
    return score



with open("highScore.txt", "r+") as hc: 
    content = hc.read().strip()
    if content == "": 
        hc.write("0")
        hc.seek(0)
    getScore = game()
    previousScore = int(content)
    if previousScore>getScore: 
        hc.seek(0)
        print(f"The score {previousScore} is greater than {getScore}")
    else: 
        hc.seek(0)
        print(f"The score {previousScore} is greater than {getScore}")
        hc.write(f"{getScore}")

