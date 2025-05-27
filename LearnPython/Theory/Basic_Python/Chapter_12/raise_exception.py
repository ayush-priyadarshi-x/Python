# Raising a ValueError if the input is not a positive number
def check_positive(number):
    if number <= 0:
        raise ValueError("The number must be positive.")
    return number

try:
    check_positive(-5)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: The number must be positive.
