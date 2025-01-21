# Creating tuples
empty_tuple = ()  # Empty tuple
single_element_tuple = (1,)  # Single element tuple (note the comma)
my_tuple = (1, 2, 3, 4)  # Tuple with multiple elements

# Accessing elements by index
print(my_tuple[1])  # Access second element; Output: 2

# Negative indexing
print(my_tuple[-1])  # Last element; Output: 4

# Slicing a tuple
print(my_tuple[1:3])  # Slice from index 1 to 2 (excludes index 3); Output: (2, 3)

# Tuple concatenation
tuple_a = (1, 2)
tuple_b = (3, 4)
concatenated = tuple_a + tuple_b  # Combines tuples; Output: (1, 2, 3, 4)

# Tuple repetition
repeated_tuple = tuple_a * 3  # Repeats tuple_a three times; Output: (1, 2, 1, 2, 1, 2)

# Checking if an element exists
print(3 in my_tuple)  # Checks if 3 is in the tuple; Output: True

# Tuple unpacking
a, b, c, d = my_tuple  # Assigns each element to a variable
print(a, b, c, d)  # Output: 1 2 3 4

# Using * to gather remaining elements
x, *y = my_tuple  # x = 1, y = [2, 3, 4]
print(x, y)  # Output: 1 [2, 3, 4]

# Using tuple as a dictionary key (immutable, so allowed)
my_dict = {("apple", "banana"): "fruits"}  # Tuples can be keys in dictionaries
print(my_dict[("apple", "banana")])  # Output: "fruits"

# Using count() and index() methods
print(my_tuple.count(2))  # Counts occurrences of 2; Output: 1
print(my_tuple.index(3))  # Finds index of first occurrence of 3; Output: 2

# Nesting tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))  # Tuple of tuples
print(nested_tuple[1][1])  # Accesses element 4; Output: 4

# Converting list to tuple
my_list = [1, 2, 3]
converted_tuple = tuple(my_list)  # Converts list to tuple; Output: (1, 2, 3)

# Immutable property
# my_tuple[1] = 10  # Uncommenting this line will raise a TypeError because tuples are immutable
