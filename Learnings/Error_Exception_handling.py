"""
1.  Compile time error ==> syntax error & indentation error
    like missing indentation or missing brackets etc.

2.  Exception ==> runtime error (errors in execution, i.e. syntax and indentation are correct)
    like zerodvision error (10/0), open(filename,'xt') file is already there so cannot be created so x is invalid
    or something is not defined.
"""


## how to handle errors ==> try-except block





try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    # with open("practice.txt", "xt") as fh: # not work as nothing in indentation indentation error
    fh = open("practice.txt","at")
    fh.write("\n")
    fh.write(str(num1))


except ZeroDivisionError:  # takes relevant exception error and execute that part only
    print("denominator cannot be zero")
except FileNotFoundError:
    print("file is not exist.")
except FileExistsError as err:
    print("file is already exist. new file with same name cannot be created")
    print(err)
except ValueError:
    print("number is not valid")
else:  ## executed if there is no error or exception found in try
    result = num1 / num2
    fh.write("\n")
    fh.write(str(result))
    fh.write("\n")
    print(result)
finally:  # this block executed every time regardless try is successful or there is exception error
    fh.close()
    fh = open("practice.txt","rt")
    print(fh.read())
    fh.close()
