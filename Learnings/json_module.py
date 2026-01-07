"""
Java Scrip Object Notation text data exchange format
Uses: API and data storage
.jason will be extension of the files
"""
import json
students = {'student1':{'roll':'101','name':'John','percent':95.5,'sports':True},
            'student2': {'roll':'102','name':'Carol','percent':92.5,'sports':False},
            'student3': {'roll':'103','name':'Bob','percent':97.5,'sports':True}}

print(students)
print(type(students))

# dump is used to write the content in jason format
# with open("student.json","wt") as fh:
#     json.dump(students,fh,indent = 2) # both works same so use only one
#     # fh.write(json.dumps(students,indent=4))
try:
    ## load data
    with open("student.json","rt") as fh:
        data = json.load(fh)
        print(data)
        print(type(data))





except FileNotFoundError:
    with open("student.json","w") as fh:
        json.dump(students,fh,indent=4)
else:
    data.update(students) ## update() to update or append the data
    with open("student.json","w") as fh:
        json.dump(data,fh,indent=4)


# students = {'student1':{'roll':'101','name':'John','percent':95.5}, # original data
#             'student2': {'roll':'102','name':'Carol','percent':92.5},
#             'student3': {'roll':'103','name':'Bob','percent':97.5}}
