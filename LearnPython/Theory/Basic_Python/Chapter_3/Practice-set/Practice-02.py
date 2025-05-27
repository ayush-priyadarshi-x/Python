letter=f""" Dear {input("Enter the Name")} 

You are selected!
                                        -{input("Enter Date")}
 """
print(letter)



# Another way 

letter=""" Dear |Name|
     You are selected! 
                       -<Date>

"""
print(letter.replace("|Name|", "Harry").replace("<Date>", "24 September "))