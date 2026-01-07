# raise exeptionName: to raise a new exception

salary = float(input("Enter your salary: "))

if salary < 0:
    # raise ValueError("Your salary cannot be negative") ## raises error
    raise Exception("Your salary cannot be negative")
else:
    print(f"yor salary is {salary}")