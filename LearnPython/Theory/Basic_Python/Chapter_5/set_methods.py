# Initial set
my_set = {1, 2, 3}
print("Original set:", my_set)

# 1. .add(element) - Adds an element to the set
my_set.add(4)
print("After add(4):", my_set)  # Output: {1, 2, 3, 4}

# 2. .remove(element) - Removes an element; raises KeyError if not found
my_set.remove(3)
print("After remove(3):", my_set)  # Output: {1, 2, 4}

# 3. .discard(element) - Removes an element if present; does nothing if not found
my_set.discard(5)  # No error even though 5 is not in the set
print("After discard(5):", my_set)  # Output: {1, 2, 4}

# 4. .pop() - Removes and returns an arbitrary element from the set
popped_element = my_set.pop()
print("Popped element:", popped_element)  # Output: 1 (or another element, since sets are unordered)
print("Set after pop():", my_set)  # Output: {2, 4} (or different elements depending on pop)

# Resetting set for further methods
my_set = {1, 2, 3}
another_set = {3, 4, 5}

# 5. .union(set) - Returns a new set with all elements from both sets
union_set = my_set.union(another_set)
print("Union of sets:", union_set)  # Output: {1, 2, 3, 4, 5}

# 6. .intersection(set) - Returns a new set with only common elements
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)  # Output: {3}

# 7. .difference(set) - Returns a new set with elements in the first set but not in the second
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)  # Output: {1, 2}

# 8. .symmetric_difference(set) - Returns a new set with elements in either set, but not in both
symmetric_difference_set = my_set.symmetric_difference(another_set)
print("Symmetric difference of sets:", symmetric_difference_set)  # Output: {1, 2, 4, 5}

# 9. .update(set) - Adds elements from another set to the current set
my_set.update(another_set)
print("Set after update with another_set:", my_set)  # Output: {1, 2, 3, 4, 5}

# Resetting set for further methods
my_set = {1, 2, 3}
another_set = {3, 4, 5}

# 10. .intersection_update(set) - Updates the set with only elements found in both
my_set.intersection_update(another_set)
print("Set after intersection_update with another_set:", my_set)  # Output: {3}

# Resetting set for further methods
my_set = {1, 2, 3}
another_set = {3, 4, 5}

# 11. .difference_update(set) - Removes elements found in another set from the current set
my_set.difference_update(another_set)
print("Set after difference_update with another_set:", my_set)  # Output: {1, 2}

# 12. .symmetric_difference_update(set) - Updates the set with elements in either set, but not both
my_set = {1, 2, 3}
my_set.symmetric_difference_update(another_set)
print("Set after symmetric_difference_update with another_set:", my_set)  # Output: {1, 2, 4, 5}

# 13. .issubset(set) - Checks if the set is a subset of another set
is_subset = {1, 2}.issubset(my_set)
print("{1, 2} is subset of my_set:", is_subset)  # Output: True or False depending on my_set

# 14. .issuperset(set) - Checks if the set is a superset of another set
is_superset = my_set.issuperset({2, 4})
print("my_set is superset of {2, 4}:", is_superset)  # Output: True or False depending on my_set

# 15. .isdisjoint(set) - Checks if two sets have no elements in common
is_disjoint = my_set.isdisjoint({6, 7})
print("my_set is disjoint with {6, 7}:", is_disjoint)  # Output: True
