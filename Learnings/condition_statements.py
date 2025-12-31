# ==, >=, <=, >, <, !=
# syntax of if
# indentation is to create block
# if condition:
#     statement1
#     statement2
#     statement3
#     ...
#     statementN
# statementM

age = float(input("What is your age? "))

# if age >= 18:
#     print("Congratulations! you are and adult. You can now cast vote !!!!")
#
# print('rest of programme')



# syntax of if else
if age >= 18:
    print("Congratulations! you are and adult. You can now cast vote !!!!")
else:
    print('A few more years before you can vote')
print('rest of programme')


#turnary operator

#true-expression if condition else false expression
num = int(input("Enter a number: "))
print("Even") if num % 2 == 0 else print("Odd")