def factorials(n): 
    if(n == 1 or n ==0 ): 
        return 1
    return n * factorials(n-1)

factorial = factorials(int(input("Enter a number : ")))
print(factorial)