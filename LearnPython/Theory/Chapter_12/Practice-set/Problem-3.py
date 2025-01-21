print("Enter a number of which you want table. ")
try: 
    user_entered_number = int(input("Enter a number"))    
except Exception as e: 
    print("You entered an incorrect format of variable. ")
multiplier = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
table = [user_entered_number*i for i in multiplier]

multiplication_table = [f"{user_entered_number} X {index + 1} = {line}" for index, line in enumerate(table) ]
with open("table.txt", "w") as f: 
    f.write(f"{multiplication_table}")
print(multiplication_table)