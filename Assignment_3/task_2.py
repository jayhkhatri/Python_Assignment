"""
task_2 use math module to calculate sqrt(n) ln(n) and sin(n)
"""

from math import sqrt, log, sin

n = float(input("Enter a number: "))
if n < 0:
    print("n is negative \n square root and natural log is undefined.")
    print(f"sine: = {sin(n)}")
elif n == 0:
    print("n is zero \n natural log is undefined.")
else:
    print(f"square root: {sqrt(n)}")
    print(f"logarithm: {log(n)}")
    print(f"sine: = {sin(n)}")