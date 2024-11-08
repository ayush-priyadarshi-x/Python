spam_messages = ["Make a lot of money", "buy now", "subscribe this", "click this"]


msg = input("Enter you comment: ")

if(not(msg in spam_messages)): 
    print("This is not a spam message. ")
else : 
    print("This is a spam message. ")