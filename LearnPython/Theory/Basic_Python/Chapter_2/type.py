# --------------------------------- Integer Conversion ---------------------------------
int_value = int("10")      # Converts string "10" to integer 10
int_value_from_float = int(3.9)  # Converts float 3.9 to integer 3 (removes decimal part)

# --------------------------------- Float Conversion ---------------------------------
float_value = float("3.14")  # Converts string "3.14" to float 3.14
float_value_from_int = float(5)  # Converts integer 5 to float 5.0

# --------------------------------- String Conversion ---------------------------------
str_value_from_int = str(100)  # Converts integer 100 to string "100"
str_value_from_float = str(3.14)  # Converts float 3.14 to string "3.14"

# --------------------------------- Boolean Conversion ---------------------------------
bool_true = bool(1)           # True, as 1 is non-zero
bool_false = bool(0)          # False, as 0 is considered False
bool_from_string = bool("Hello")  # True, non-empty string
bool_from_empty_string = bool("") # False, empty string

# --------------------------------- List Conversion ---------------------------------
list_from_string = list("abc")  # Converts string "abc" to list ['a', 'b', 'c']
list_from_tuple = list((1, 2, 3)) # Converts tuple (1, 2, 3) to list [1, 2, 3]

# --------------------------------- Tuple Conversion ---------------------------------
tuple_from_list = tuple([1, 2, 3])  # Converts list [1, 2, 3] to tuple (1, 2, 3)
tuple_from_string = tuple("abc")    # Converts string "abc" to tuple ('a', 'b', 'c')

# --------------------------------- Set Conversion ---------------------------------
set_from_list = set([1, 2, 2, 3])  # Converts list [1, 2, 2, 3] to set {1, 2, 3} (removes duplicates)
set_from_string = set("hello")     # Converts string "hello" to set {'h', 'e', 'l', 'o'} (duplicates removed)


# --------------------------------- Type() ---------------------------------
# Check the type of different values
print(type(10))           # <class 'int'> (integer)
print(type(3.14))         # <class 'float'> (floating-point)
print(type("Hello"))      # <class 'str'> (string)
print(type([1, 2, 3]))    # <class 'list'> (list)
print(type((1, 2, 3)))    # <class 'tuple'> (tuple)
print(type({1, 2, 3}))    # <class 'set'> (set)
print(type({"name": "Ayush"}))  # <class 'dict'> (dictionary)
print(type(None))         # <class 'NoneType'> (null or undefined type)




