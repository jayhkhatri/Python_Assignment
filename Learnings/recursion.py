"""
Recursion is a process in which a function calls itself till a certain condition is met.
factorial of n => n*(n-1)*(n-2)*...*2*1

there are 2 parts of any recursive function
1. base/terminal condition (to stop calling it self to avoid infinite calling
2. the recursive condition

"""
# without recursion
def factorial(n):
    factorialval = 1
    if n == 0:
        return 1
    while n>1:
        factorialval *= n
        n -= 1
    return factorialval
num = 0
fact = factorial(num)
print(f"factorial of {num} is {fact}")


# with recursion
def factorialr(n):
    if n == 0:
        return 1
    else:
        factorialval1 = n*factorialr(n-1)
    return factorialval1
num = 0
fact = factorial(num)
print(f"factorial of {num} is {fact}")