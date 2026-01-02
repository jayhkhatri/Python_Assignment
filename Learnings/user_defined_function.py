"""
syntax
def funct_name(arguments)
    statements
    statements
    statements



"""

def greeting_someone(name):
    print(f"Hello {name}, good morning")
    print("it's a beautiful day")

# calling function within function block
greeting_someone('John')



def add(num1, num2):
    result= num1 + num2
    print(f"Result is {result}")


add(10,5)


# return a value from function

def add(num1, num2):
    return num1 + num2


a =10
b = 5
C = add(a,b)
print(f"sum of {a} and {b} is {C}")


def arithmatic(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    return addition, subtraction, multiplication

sum1, sub1, mult1 = arithmatic(a,b)
print(f"sum of {a} and {b} is {sum1}")
print(f"subtraction of {a} and {b} is {sub1}")
print(f"multiplication of {a} and {b} is {mult1}")
