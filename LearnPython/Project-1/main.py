import random

def computerChoice(): 
    return random.choice([0, 1, -1])

userChoice = input("Enter what you want to choose between snake, water, and gun (s/w/g): ").strip().lower()

# Mapping of user inputs to the internal numeric values
userChoiceManual = {"s": 1, "snake": 1, "w": -1, "water": -1, "g": 0, "gun": 0}

# Validate and convert user choice
if userChoice not in userChoiceManual:
    print("Invalid input. Please enter 's', 'w', or 'g'.")
else:
    userChoiceValue = userChoiceManual[userChoice]
    choosenComputerChoice = computerChoice()

    # Print choices for clarity
    print(f"You chose: {userChoice}")
    print(f"Computer chose: {['gun', 'snake', 'water'][choosenComputerChoice]}")

    # Determine the result
    if userChoiceValue == choosenComputerChoice:
        print("It's a draw.")
    elif userChoiceValue == 1:  # User chose Snake
        if choosenComputerChoice == -1:
            print("You won! Computer lost with water.")
        elif choosenComputerChoice == 0:
            print("You lost! Computer won with gun.")
    elif userChoiceValue == -1:  # User chose Water
        if choosenComputerChoice == 0:
            print("You won! Computer lost with gun.")
        elif choosenComputerChoice == 1:
            print("You lost! Computer won with snake.")
    elif userChoiceValue == 0:  # User chose Gun
        if choosenComputerChoice == 1:
            print("You won! Computer lost with snake.")
        elif choosenComputerChoice == -1:
            print("You lost! Computer won with water.")
