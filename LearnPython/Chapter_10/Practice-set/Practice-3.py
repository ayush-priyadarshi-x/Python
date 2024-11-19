class Demo: 
    a = 1

something = Demo()
print(f"a for Class attribute : {something.a }")
something.a = 0
print(f"a after instance attribute : {something.a}")

print(f"a without any instance : {Demo.a}")