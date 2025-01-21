numbers = [1,2,3,4,5, 10, 15]

factors = list(filter(lambda x: x%5 ==0, numbers))
print(factors)