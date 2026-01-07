"""
will create function to take input for show balance withdrawal and deposit in account

"""
balance =0.0
kyc_dictionary = {'Aadhar_Card':'', 'PAN_Card':'', 'Address':'', 'photo':'', 'signature':''}

def check_balance():
    print(f"Checking balance {balance}")
    print("=============================")



def deposit(amount):
    print(f"Depositing an amount {amount}")
    global balance
    if amount <= 0:
        print("Can not deposit negative or zero amounts")
        print("=============================")
    else:
        balance = balance + amount
        print(f"amount {amount} is deposited successfully")
        check_balance()



def withdraw(amount):
    global balance
    print(f"Withdrawing an amount {amount}")
    if amount <= 0:
        print("can not withdraw negative or zero amounts")
        print("=============================")
    else:
        balance = balance - amount
        print(f"amount {amount} is withdrawn successfully")
        check_balance()
    if balance < 0:
        print("You cannot withdraw amounts > remaining balance. \n insufficient balance")
        print("=============================")

def update_kyc(doc1):
    global kyc_dictionary
    kyc_dictionary.update(doc1)

def check_kyc():
    for doc2 in kyc_dictionary:
        print(f"{doc2} : {kyc_dictionary[doc2]}")

if __name__ == "__main__":
    print("=============================")
    print("Welcome to the Banking App")
    print("=============================")

    while True:
        print("1. check your balance")
        print("2. deposit an amount")
        print("3. withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = int(input("Enter your choice: "))
        print("=============================")

        if choice == 1:
            check_balance()
        elif choice == 2:
            # print("Enter the amount you want to deposit")
            amt = float(input("Enter the amount you want to deposit: "))
            deposit(amt)
        elif choice == 3:
            # print("Enter the amount you want to withdraw")
            amt = float(input("Enter the amount you want to withdraw: "))
            withdraw(amt)
        elif choice ==6:
            break
        elif choice ==4:
            if all(ele == '' for ele in kyc_dictionary.values() ):
                print("KYC is not done, \nDo KYC as earliest")
            else:
                for doc in kyc_dictionary:
                    print(f"{doc}:{kyc_dictionary[doc]}")
        elif choice ==5:  # update KYC
            kyc_doc = {}
            print("==================================================")
            print("A. Aadhaar Update")
            print("B. PAN card update")
            print("C. Address")
            print("D. Photo")
            print("E. signature")
            print("==================================================")
            doc = list(input("Enter your choices: eg. ABDE (without space) \n "))
            for i in doc:
                if i.upper() == "A":
                    key = 'Aadhar_Card'
                    value = input(f"Enter the Aadhar card number: {i.upper()} ")
                    # update_kyc(key=value)
                elif i.upper() == "B":
                    key = 'PAN_Card'
                    value = input(f"Enter the PAN card number: {i.upper()} ")
                    # update_kyc(key=value)
                elif i.upper() == "C":
                    key = 'Address'
                    value = input(f"Enter the Address: {i.upper()} ")
                elif i.upper() == "D":
                    key = 'photo'
                    value = input(f"Enter the PHOTO number: {i.upper()} ")
                elif i.upper() == "E":
                    key = 'signature'
                    value = input(f"Enter the signature number: {i.upper()} ")
                else:
                    print(f"{i} is not a valid choice hence skipped")

                kyc_doc[key] = value
            print(kyc_doc)

            update_kyc(kyc_doc)
            print("KYC update successful")
            check_kyc()


        else:
            print("Please enter a valid choice")
    print("=============================")
    print("Thank you for using this application")