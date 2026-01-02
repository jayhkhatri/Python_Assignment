# l = ['mike', 10.2, 1980]
# l='apple'
l = range(1,11)


print(l)


for items in l:
    print(items)


s1 = "Hello world"
for char in s1:
    print(char)
print("end of loop")

employee = {'empid':1001,'name': "John Gray",'department':"HR"}

for key, value in employee.items():
    print(key, value)
for i in employee:
    print(i,employee[i])

for i in employee.items():
    print(i)