"""
simple interest I = (P*R*T)/100
P = principal amount
R = real interest rate
T = Time duration

"""

principal = float(input("Enter the principal amount: "))
Rate = float(input("Enter the real interest rate: "))
T = float(input("Enter the time duration: "))


SI = (principal*Rate*T)/100

print('Simple interest is: ', SI)