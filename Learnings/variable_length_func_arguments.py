# *arg - allows variable length positional arguments
def add(*args):
    """
    give the arguments either in int and/or float, it will calculate the sum and return it.
    """
    return sum(args)

result = add(1,2,3,4,5,6,7,8,9)
print(result)
print(help(add))

# variable length position arguments
def student_details(sid,name,*marks):
    if len(marks)==0:
        print(f"{name} with id {sid} was absent in all the exams")
        return 'Absent'
    else:
        percentage = sum(marks)/len(marks)
        return percentage


john = student_details(101,'John',87.0, 69.5, 81.5, 74.0)
Carol =student_details(102,'carol',91.0, 49.5, 91.5, 84.0, 86.5)
Mark = student_details(103,'Mark')

print(john)
print(Carol)
print(Mark)


# variable length keyword arguments

def func(**kwargs):
    print(kwargs)


func(a=1,b=2,c=3,d=4,e=5,f=6,g=7)



def student_details(sid,name,**marks):
    if len(marks)==0:
        print(f"{name} with id {sid} was absent in all the exams")
        return 'Absent'
    else:
        percentage = sum(marks.values())/len(marks)
        return percentage


john = student_details(101,'John',eng=87.0, phy=69.5, chem=81.5, maths=74.0)
Carol =student_details(102,'carol',eng=91.0, phy=49.5,chem=91.5, maths=84.0, comp=86.5)
Mark = student_details(103,'Mark')

print(john)
print(Carol)
print(Mark)


def student_details(sid,name,*args,**marks):
    if len(args)==0:
        A = 'not playing'
    else:
        A = list (args)
    if len(marks)==0:
        print(f"{name} with id {sid} was absent in all the exams")
        return 'Absent',A
    else:
        percentage = sum(marks.values())/len(marks)
        return percentage,A


john, jsports = student_details(101,'John','cricket',eng=87.0, phy=69.5, chem=81.5, maths=74.0)
Carol, Csports =student_details(102,'carol','football',eng=91.0, phy=49.5,chem=91.5, maths=84.0, comp=86.5)
Mark, ksports  = student_details(103,'Mark')

print(f"John gets {john}% and plays {jsports}")
print(f"Carol gets {Carol}% and plays {Csports}")
print(f"Mark gets {Mark}% and plays {ksports}")

