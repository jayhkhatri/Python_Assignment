"""
python program that opens and read text file and handles error gracefully if fide doesn't exist

"""
def reading_file(name):
    try:
        with open(name, "r") as fh:
            print("reading file content:")
            print(fh.read())
    except FileNotFoundError:
        print(f"File {name} not found :")
        # raise FileNotFoundError(f"File {name} not found")




if __name__ == "__main__":
    name1 = "new_file.txt"
    reading_file(name1)