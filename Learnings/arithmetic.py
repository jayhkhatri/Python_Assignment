"""
A simple arithmatic module:

"""

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def power(a,b):
    return a**b

def square(a):
    return a**2

def cube(a):
    return a**3

def square_root(a):
    return a**(1/2)

def cube_root(a):
    return a**(1/3)

#__name__ variable


# a = 10
# b = 20
# print(add(a,b))  # this will also be printed even though this was not called.
# print(subtract(a,b))
print(f"__name__ value in arithmetic.py => {__name__}")
# so we want to avoid this and we use __name__ variable
if __name__ == '__main__': ## this will not execute when module is imported.
# for userdefinmodule_calling.py => __name__  => "__main__"
# for arithmetic.py => __name => "arithmetic" not as main so if condition fails and the code will not execute.
    a = 10
    b = 20
    print(add(a,b))
    print(subtract(a,b))