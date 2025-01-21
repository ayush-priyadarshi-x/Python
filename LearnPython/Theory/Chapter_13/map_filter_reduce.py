from functools import reduce  # Import reduce

# Map
l = [1, 2, 3]
square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter
even = lambda x: x%2==0

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce
csum = lambda a,b: a+b
print(reduce(csum, l))