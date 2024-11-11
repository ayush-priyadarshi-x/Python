enteredNumber = int(input("Enter the number : "))
rangeNumber = enteredNumber + 1

for i in range(1, rangeNumber):
    if(i == 1 ): 
        continue
    elif(i== enteredNumber): 
        continue 
    elif(rangeNumber%i == 0 ): 
        print("The given number is not a prime number.")
        break
    else: 
        print("The given number is prime number. ")
        break
        