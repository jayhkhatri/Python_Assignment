# Opening file in python
# open(file_name,mode)
# modes: r -read, x-create, w-write or overwrite, a -append
import os
from os import remove
from pathlib import Path

file_handler = open("practice.txt", "tr")
print(file_handler.read()) ## read() will read the content as string in t mode.


# closing the file
file_handler.close()


## create a file
file_handler1 = open("practice1.txt", "xt") # since file does not exist it will create one
file_handler1.write("hello world\n") # to write inside a file
file_handler1.write("\nThis is a new one.")
file_handler1.write("\nThis is a test one.")
file_handler1.close()
print(file_handler1) # this will give some basic data with pointer at start of file


## reading mode r

file_handler2 = open("practice.txt", "tr")
reading = file_handler2.read(5)
reading1 = file_handler2.readline() # this will read lines one by one in sequence of call if line was not there is produce empty str output
reading2 = file_handler2.readline()
reading3 = file_handler2.readline()
file_handler2.close()
print(reading, type(reading))
print(f"Line 1 is: {reading1}")
print(f"Line 2 is: {reading2}")
print(f"Line 3 is: {reading3}")


Fh3 = open("practice.txt", "rt")
readings = Fh3.readlines() # fetch all the lines.
Fh3.close()
print(readings)
print(type(readings)) # data type is list. i.e. all the lines are stored as single list.
print(readings[0])
for lines in readings:
    print(lines.rstrip('\n'))






## w mode
fh = open("practice1.txt",'tw') # w mode will delete the existing content inside the file so be very carefull wille calling a file with w
# if the file does not exist it will create the file.

fh.write("hello world.\nThis is a new one.")
fh.close()

fh = open("practice1.txt",'rt')
print(fh.read())
fh.close()
# remove("practice1.txt")
# remove("practice2.txt")



## Appending into a file
Appending = open("practice1.txt",'at') # incase file does not exist it will also create a new file.
Appending.write("\nHello world.\nThis is a added one.") # with append mode a f.write will append the str at the end of the file.
Appending.close()

fh = open("practice1.txt",'rt')
print(fh.read())
fh.close()
remove("practice1.txt")



## with function
with open("practice.txt",'rt') as fh:
    content = fh.read()  # here it will take care open and closing of file with while inside matter will be require to update.
    # with statement will automatically close the file even in the case of error.

print(content)

## checking if file exist or not.

file_name = "D:/akash vyas/Doosan_Robotics_Robot_A0509S_IGES_200824.SLDPRT"  # use front slashes inspace of backslash
if os.path.exists(file_name):
    print("file exists")
else:
    print("file does not exist")

# os.path.exists():  to check file or directory exist there or not.


# pathlib.path.exists function  2nd method
file_name1 = Path("D:/akash vyas/Doosan_Robotics_Robot_A0509S_IGES_200824.SLDPRT")
if file_name1.exists():
    print("file exists. cannot create a new file")
else:
    print("file does not exist, creating a new file")
    fh = open(file_name1,'wt')
    fh.write("hello world.\nThis is a new one.")
    fh.close()

file_name1 = Path("D:/new.txt")
if file_name1.exists():
    print("file exists. cannot create a new file")
else:
    print("file does not exist, creating a new file")
    fh = open(file_name1,'wt')
    fh.write("hello world.\nThis is a new one.")
    fh.close()
    fh = open(file_name1,'rt')
    print(fh.read())

#remove(file_name1)