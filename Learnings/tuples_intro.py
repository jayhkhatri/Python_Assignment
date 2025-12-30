# sequence of item in () brackets
#(item1,item2,.....)

# we can not modify the tuple like append, index, sort, sum,max, min,etc.

t1 = ("python", 10,1.5,True,[1,2,4],(10,20))
print(t1)
print(type(t1))

t1 = "python", 10,1.5,True,[1,2,4],(10,20)
print(t1)
print(type(t1))

t2 = ["python", 10,1.5,True,[1,2,4],(10,20)]
print(t2)
print(type(t2))

t2 = tuple(t2)
print(t2)
print(type(t2))

t2 = list(t2)
print(t2)
print(type(t2))

# tuple operations


student_details1 = (1001,"John")
student_details2 = (78.5,91.0,83.5,79.5)


student_detail = student_details1+student_details2
print(student_detail)
student_detail = student_details1+5*student_details2
print(student_detail)

print(1001 in student_detail)
print(78.5 not in student_detail)


# mutability and immutability
# list are mutable while tuples and strings are immutable

s1 = "python is fun"
s1.replace("python","Java")
print(s1)