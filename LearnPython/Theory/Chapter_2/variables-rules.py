# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_)
name = "Ayush"       # Valid
_age = 25            # Valid

# 2. Variable names cannot start with a number
# 3age = 30          # Invalid

# 3. Variable names can only contain letters, numbers, and underscores (no special characters like @, $, %)
age1 = 30            # Valid
total_score = 100    # Valid
# total-score = 100  # Invalid

# 4. Variable names are case-sensitive, meaning age and Age are different variables
Age = 20
age = 25             # 'Age' and 'age' are treated as separate variables

# 5. Avoid using Python keywords or built-in function names as variable names
# class = "Math"     # Invalid, because 'class' is a Python keyword
print = 50           # Avoid using 'print' since it's a built-in function name

# 6. Use descriptive names that make the code easier to read
num_apples = 10      # Good practice
