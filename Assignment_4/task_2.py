"""
task_2 python program to input, amend ,read and display data
"""
from task_1 import reading_file

def write_file(name,content):
    with open(name,'w') as file:
        file.write(content)
        file.write("\n")
        print(f"Data successfully written to {name}")

def append_file(name,content):
    with open(name,'a') as file:
        file.write(content)
        file.write("\n")
        print(f"file {name} appended successfully")


def create_file(name):
    try:
        with open(name,'x') as file:
            print(f"file {name} created successfully")
    except FileExistsError:
        # print(f"File {name} already exists")
        raise FileExistsError("File already exists, can not creat the file try to write or amend it")

def final_content(name):
     try:
         print(f"Final content of file {name}:")
         reading_file(name)
     except FileNotFoundError:
         print("")

 # with open(name,'r') as file:
 #     print(f"Fina Content of {name}:")
 #     print(file.read())

if __name__ == "__main__":
    name1 = "new_file1.txt"
    content1 = "Hello World"
    create_file(name1)
    write_file(name1,content1)
    append_file(name1,content1)
    final_content(name1)

