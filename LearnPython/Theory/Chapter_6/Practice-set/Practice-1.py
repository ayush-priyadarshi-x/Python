# Initialize an empty list
enteredNumbers = []

# Collect 4 numbers from the user
enteredVal = int(input("Enter the number: "))
enteredNumbers.append(enteredVal)

enteredVal = int(input("Enter the number: "))
enteredNumbers.append(enteredVal)

enteredVal = int(input("Enter the number: "))
enteredNumbers.append(enteredVal)

enteredVal = int(input("Enter the number: "))
enteredNumbers.append(enteredVal)

# Initialize greatest with the first number
greatest = enteredNumbers[0]

# Compare the numbers using if-else statements
if enteredNumbers[1] > greatest:
    greatest = enteredNumbers[1]

if enteredNumbers[2] > greatest:
    greatest = enteredNumbers[2]

if enteredNumbers[3] > greatest:
    greatest = enteredNumbers[3]

# Print the greatest number
print("The greatest number is:", greatest)
