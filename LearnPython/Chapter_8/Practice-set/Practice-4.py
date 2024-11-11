def sumNatural(n): 
    if(n==1 ): 
        return 1 
    elif(n==0): 
        return 0
    sum = n + sumNatural(n-1)
    return sum

sumOfEnteredNumber = sumNatural(int(input("Enter the digit. ")))
print(f"The sum of the given natural number : {sumOfEnteredNumber}")