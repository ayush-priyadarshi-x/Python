import random
computer_guessed_number = random.randint(1, 100)

user_guessed_number = int(input("Guess a number in the interval [1, 100]"))

number_of_guesses = 1

while user_guessed_number != computer_guessed_number: 
    number_of_guesses += 1
    if user_guessed_number>computer_guessed_number: 
          print("You guessed a higher number . ")
    else: 
          print("You guessed a lower number . ")
    user_guessed_number = int(input("Guess a number in the interval [1, 100]"))



print("You guessed correct number . ")
print(f"Number of guesses required: {number_of_guesses}")
print(f"Computer guessed: {computer_guessed_number} \n User guessed: {user_guessed_number}")