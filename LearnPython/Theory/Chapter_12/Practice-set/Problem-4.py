try: 
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    try: 
       print( a/b )
    except ZeroDivisionError as e: 
        print(e)
except ValueError as e: 
    print("Wrong format for a or b. ")