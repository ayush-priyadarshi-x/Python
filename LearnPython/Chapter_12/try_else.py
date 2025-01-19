try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Handle specific exception
    print("Cannot divide by zero.")
else:
    # Code to execute if no exception occurred
    print("Division successful! Result:", result)
