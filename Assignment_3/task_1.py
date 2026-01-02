"""
Task 1 calculating the factorial
here function first ask for user input and then calculate its factorial using recursive function
"""

num1 = int(input("Enter a number: "))

def factorial(n):
    if n < 0:
        print("factorial of negative number is not defined. kindly provide a valid positive integer ")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


Num_factorial = factorial(num1)

print(f"factorial of {num1} is: {Num_factorial}")