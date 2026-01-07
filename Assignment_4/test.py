## task 1 is done here

from task_1 import reading_file
import task_2 as t2

print("Task 1")
name1 = "new_file.txt"
reading_file(name1)

# if file not found
name = "new_file1.txt"
reading_file(name)

print("\n \n \n Task 2")
## task_2 is done here.
## creating file if not exist
name = "output.txt"
t2.create_file(name)

## writing file in w mode
content = "Hello python"
t2.write_file(name, content)

## appending the file
content1 = "Learning file handling in python."
t2.append_file(name, content1)

## final reading
t2.final_content(name)