# Initialize a list
my_list = [1, 2, 3]

# Append an item
my_list.append(4)  # [1, 2, 3, 4]

# Extend the list with another list
my_list.extend([5, 6])  # [1, 2, 3, 4, 5, 6]

# Insert an item at a specific index
my_list.insert(1, 'a')  # [1, 'a', 2, 3, 4, 5, 6]

# Remove an item by value
my_list.remove('a')  # [1, 2, 3, 4, 5, 6]

# Pop an item by index (default is last)
my_list.pop()  # Removes 6; result: [1, 2, 3, 4, 5]

# Find index of an item
index_of_4 = my_list.index(4)  # 3

# Count occurrences of an item
count_of_2 = my_list.count(2)  # 1

# Sort the list in ascending order
my_list.sort()  # [1, 2, 3, 4, 5]

# Reverse the order of the list
my_list.reverse()  # [5, 4, 3, 2, 1]

# Clear all items from the list
my_list.clear()  # []
