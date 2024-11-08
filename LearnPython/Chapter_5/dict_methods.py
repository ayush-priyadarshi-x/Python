# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)

# 1. .clear() - Removes all items
my_dict.clear()
print("After clear():", my_dict)  # Output: {}

# Resetting dictionary for further methods
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 2. .copy() - Creates a shallow copy
copy_dict = my_dict.copy()
print("Copy of dictionary:", copy_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 3. .get(key, default) - Gets the value for a key; returns default if key not found
value = my_dict.get('b', 0)
print("Value for key 'b':", value)  # Output: 2
value_not_found = my_dict.get('z', 0)
print("Value for non-existent key 'z':", value_not_found)  # Output: 0

# 4. .items() - Returns a view of dictionary's key-value pairs
items = my_dict.items()
print("Items view:", items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 5. .keys() - Returns a view of all keys
keys = my_dict.keys()
print("Keys view:", keys)  # Output: dict_keys(['a', 'b', 'c'])

# 6. .values() - Returns a view of all values
values = my_dict.values()
print("Values view:", values)  # Output: dict_values([1, 2, 3])

# 7. .pop(key, default) - Removes key and returns its value; returns default if key not found
popped_value = my_dict.pop('a', None)
print("Popped value for key 'a':", popped_value)  # Output: 1
print("Dictionary after pop('a'):", my_dict)  # Output: {'b': 2, 'c': 3}

# 8. .popitem() - Removes and returns an arbitrary key-value pair (LIFO for Python 3.7+)
popped_item = my_dict.popitem()
print("Popped item:", popped_item)  # Output: ('c', 3) or ('b', 2), depending on Python version
print("Dictionary after popitem():", my_dict)  # Output: {'b': 2} or {'c': 3}

# Resetting dictionary for further methods
my_dict = {'a': 1, 'b': 2}

# 9. .setdefault(key, default) - Returns the value of key if it exists; otherwise sets it to default
default_value = my_dict.setdefault('d', 4)
print("Value for key 'd' (after setdefault):", default_value)  # Output: 4
print("Dictionary after setdefault('d', 4):", my_dict)  # Output: {'a': 1, 'b': 2, 'd': 4}

# 10. .update(dict2) - Updates the dictionary with key-value pairs from another dictionary
my_dict.update({'b': 20, 'e': 5})
print("Dictionary after update({'b': 20, 'e': 5}):", my_dict)  # Output: {'a': 1, 'b': 20, 'd': 4, 'e': 5}
