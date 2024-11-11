def greatest(a, b, c): 
    greatest = a 
    if greatest < b: 
        greatest = b
    if greatest < c: 
        greatest = c
    
    return greatest

def inputNum(): 
    return int(input("Enter the number: "))

# Call inputNum() to get the actual numbers
someNums = greatest(inputNum(), inputNum(), inputNum())
print(f"The greatest is: {someNums}")
