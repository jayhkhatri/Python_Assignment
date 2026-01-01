import arithmetic


print(f"__name__ value in userdefinemodule_calling.py => {__name__}")
a = 100
b= 20

Sumresult = arithmetic.add(a,b)
Subresult = arithmetic.subtract(a,b)
Multresult = arithmetic.multiply(a, b)
Divresult = arithmetic.divide(a, b)

print(Sumresult)
print(Subresult)
print(Multresult)
print(Divresult)