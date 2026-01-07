"""
when we need to store list, tuple, dictionary, etc. in computer we need to convert them to byte (call serialization)
and to access that we need to conver bytes to data (deserialization)



"""

students = {'student1':{'roll':'101','name':'John','percent':95.5},
            'student2': {'roll':'102','name':'Carol','percent':92.5},
            'student3': {'roll':'103','name':'Bob','percent':97.5}}
print(type(students))
with open("student_info.txt","wt") as fh:
    fh.write(str(students))  # need to convert data type from dic to str so not reversible.

with open("student_info.txt","rt") as fh:
    contents = fh.read()

print(type(contents))
# out = dict(contents) # throws error and hence we lost the dict data type here

import pickle

# serialization
with open("student_info.bin","wb") as fh:  # works with binary file, bin or dat
    for student in students:
        pickle.dump(students[student],fh)

# deserialization
with open("student_info.bin","rb") as fh:
    while True: ## can use for loop as well
        try:
            data = pickle.load(fh)
            print(data)
            print(type(data))
        except EOFError:
            print("Done")
            break
    #
    # data1 = pickle.load(fh)
    # print(data1)
    # print(type(data1))
    # data2 = pickle.load(fh)## we gate data one by one
    # print(data2)
    # print(type(data2))
    # data3 = pickle.load(fh)
    # print(data3)
    # print(type(data3))

## print the name of students who secure 95 or more percent
new_list_95= []
with open("student_info.bin","rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['percent'] > 95:
                new_list_95.append(data['name'])
        except EOFError:
            print("Done")
            break

print(f"The list of students who got more than 95 are {new_list_95}")
