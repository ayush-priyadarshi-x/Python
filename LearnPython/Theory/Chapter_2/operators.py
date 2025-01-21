# --------------------------------- Arithmetic Operators ---------------------------------
x = 10
y = 3

add = x + y          # Addition
sub = x - y          # Subtraction
mul = x * y          # Multiplication
div = x / y          # Division (returns float)
floor_div = x // y   # Floor Division
mod = x % y          # Modulus
exp = x ** y         # Exponentiation

# --------------------------------- Assignment Operators ---------------------------------
a = 5                # Assigns 5 to a
a += 2               # Equivalent to a = a + 2; now a is 7
a -= 1               # Equivalent to a = a - 1; now a is 6
a *= 3               # Equivalent to a = a * 3; now a is 18
a /= 6               # Equivalent to a = a / 6; now a is 3.0
a //= 2              # Equivalent to a = a // 2; now a is 1.0
a %= 3               # Equivalent to a = a % 3; now a is 1.0
a **= 2              # Equivalent to a = a ** 2; now a is 1.0

# --------------------------------- Comparison Operators ---------------------------------
x = 5
y = 10

eq = (x == y)        # Equal to
neq = (x != y)       # Not equal to
gt = (x > y)         # Greater than
lt = (x < y)         # Less than
gte = (x >= y)       # Greater than or equal to
lte = (x <= y)       # Less than or equal to

# --------------------------------- Logical Operators ---------------------------------
x = True
y = False

and_op = x and y     # True if both are true
or_op = x or y       # True if at least one is true
not_op = not x       # Reverses boolean value
not(x) # False
not(y) # True

# --------------------------------- Bitwise Operators ---------------------------------
a = 5                # 0b0101 in binary
b = 3                # 0b0011 in binary

bitwise_and = a & b  # Bitwise AND
bitwise_or = a | b   # Bitwise OR
bitwise_xor = a ^ b  # Bitwise XOR
bitwise_not = ~a     # Bitwise NOT
left_shift = a << 1  # Left Shift
right_shift = a >> 1 # Right Shift

# --------------------------------- Identity Operators ---------------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

is_op = (a is b)     # True if both refer to the same object
is_not_op = (a is not c)  # True if both do not refer to the same object

# --------------------------------- Membership Operators ---------------------------------
fruits = ["apple", "banana", "cherry"]

in_op = "banana" in fruits   # True if the value is in the list
not_in_op = "grape" not in fruits  # True if the value is not in the list
