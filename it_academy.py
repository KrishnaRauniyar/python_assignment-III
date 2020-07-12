# B. Create a console application for an IT Academy with the
# following features:
# a) The academy program should have a fixed course of study. b) If a new student is interested in the academy program the student can
# inquiry about the course of study. c) Student Registration with Rs. 20000 (deposit). Students are allowed to
# pay in two installments with Rs. 10000 each. d) Display all the student’s information from the academy with their payments
# and remaining payments. e) Update the student information if needed. f) Delete the student information if he/she left the program. g) Return the deposit amount (Rs. 20000) to the students after the successful completion of the course and check the balance.
# Remember it should be a full feature CONSOLE APP. You can store the course of study and the student’s detail in your preferred file format (.csv, .txt, etc). Ignore the permissions for now. Anyone who runs the script is allowed to access all the features. Develop the app with OOP Approach.


import pickle
import os
import pathlib


class Account:
    number = 0
    name = ''
    course = ''
    deposit = 0

    def createAccount(self):
        self.name = input("Enter your name : ")
        self.number = int(input("Enter your phone number : "))
        self.course = input("Enter the course you are interested in(html/css/js/python/django): ")
        self.deposit = int(input("Enter the amount(Rs. 20000 for Registration or Rs. 10000 partial payment): "))
        print("\n\n\nAccount Created")

    def showAccount(self):
        print("Your phone number: ", self.number)
        print("Account Holder Name : ", self.name)
        print("Name of Course", self.course)
        print("Balance : ", self.deposit)

    def updateAccount(self):
        print("Phone Number : ", self.number)
        self.name = input("Update Account Holder Name :")
        self.course = input("Update the type of Course :")
        self.deposit = int(input("Update Balance :"))

    def depositAmount(self, amount):
        self.deposit += amount

    def receiveAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(self.number, " ", self.name, " ", self.course, " ", self.deposit)

    def getAccountNo(self):
        return self.number

    def getAccountHolderName(self):
        return self.name

    def getAccountCourse(self):
        return self.course

    def getDeposit(self):
        return self.deposit


def intro():
    print("\t\t\t\t\t\t\t\t\t\t\t********WELCOME TO********")
    print("\t\t\t\t\t\t\t\t\t\t\t****My NUMBER ONE ACADEMY****")
    input()


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("it_file.csv")
    if file.exists():
        infile = open('it_file.csv', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.number, " ", item.name, " ", item.course, " ", item.deposit)
        infile.close()
    else:
        print("No records to display")


def displaySp(num):
    file = pathlib.Path("it_file.csv")
    if file.exists():
        infile = open('it_file.csv', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.number == num:
                print("Your deposited balance is = ", item.deposit)
                found = True
    else :
        print("No records to Search")
    if not found:
        print("No existing record with this number")


def depositAndWithdraw(num1, num2):
    file = pathlib.Path("it_file.csv")
    if file.exists():
        infile = open('it_file.csv', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('it_file.csv')
        for item in mylist:
            if item.number == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.deposit += amount
                    print("Your account is updated")
                elif num2 == 2:
                    amount = int(input("Enter the amount to take back : "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                    else:
                        print("You cannot withdraw more than Rs. 20000")
    else:
        print("No records to Search")

    outfile = open('new_it_file.csv', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('new_it_file.csv', 'it_file.csv')


def deleteAccount(num):
    file = pathlib.Path("it_file.csv")
    if file.exists():
        infile = open('it_file.csv', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist:
            if item.number != num:
                newlist.append(item)
        os.remove('it_file.csv')
        outfile = open('new_it_file.csv', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('new_it_file.csv', 'it_file.csv')


def updateAccount(num):
    file = pathlib.Path("it_file.csv")
    if file.exists():
        infile = open('it_file.csv', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('it_file.csv')
        for item in oldlist:
            if item.number == num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the Course name : ")
                item.deposit = int(input("Enter the Amount : "))

        outfile = open('new_it_file.csv', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('new_it_file.csv', 'it_file.csv')


def writeAccountsFile(account):
    file = pathlib.Path("it_file.csv")
    if file.exists():
        infile = open('it_file.csv', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('it_file.csv')
    else:
        oldlist = [account]
    outfile = open('new_it_file.csv', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('new_it_file.csv', 'it_file.csv')


ch = ''
num = 0
intro()

while ch != 8:
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT (Refundable)")
    print("\t3. WITHDRAW AMOUNT AFTER COMPLETION OF COURSE")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. DELETE AN ACCOUNT")
    print("\t7. UPDATE AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input()

    if ch == '1':
        writeAccount()
    elif ch == '2':
        num = int(input("\tEnter the phone number : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter the phone number : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter the phone number : "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num = int(input("\tEnter the phone number : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter the phone number : "))
        updateAccount(num)
    elif ch == '8':
        print("\tThanks for choosing My NUMBER ONE ACADEMY")
        break
    else:
        print("Invalid choice")

    ch = input("Enter your choice : ")




