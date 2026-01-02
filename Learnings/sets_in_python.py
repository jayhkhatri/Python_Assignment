# sets are non-sequential collection of items.
# comma separated elements enclosed within {}
# indexing is not allowed in this type of class
# do not allow duplicate elements or multiple elements in same set
from Learnings.tuples_intro import student_details2

set1 = {10,"python",2.5,10}
print(set1)
print(type(set1))

# sets are mutable

set1.add(45)
print(set1)

set1.remove("python")
print(set1)

set1.discard(10)
print(set1)

set1.discard(145)
print(set1) # no error as 145 not in the listedCountry to be discarded so no worries like remove



student1= {"English","Maths","Computer science","biology","physics"}
print(student1)
print(type(student1))
student2 = {"english","biology","chemistry","physics"}
print(student2)
print(type(student2))

# union
all_subjects = student1.union(student2)
all_same_subjects = student1 | student2
print(f"list of all the subjects are {all_subjects}")
print(f"list of all the subjects are {all_same_subjects}")
# intersection
common_subject = student1.intersection(student2)
print(f"list of common subjects are \t {common_subject}")

# difference
diffstd1 = student1.difference(student2)
d1 =student1-student2

diffstd2 = student2.difference(student1)
d2 = student2-student1
print(f"student1 studies \t{diffstd1} \t subjects apart from students2")
print(d1)
print(f"student2 studies \t{diffstd2} \t subject separately from student1")


fs1 = frozenset(student1)
print(fs1,type(fs1))