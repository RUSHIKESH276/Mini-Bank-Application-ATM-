class Customer:
    bankname="SBI Bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("After deposit balance is",self.balance)
    def withdrawl(self,amount):
        if amount>self.balance:
            print("Insuffcient balance {} you can't perform the operation!!".format(self.balance))
        else:
            self.balance=self.balance-amount
            print("After withdrawl balance is",self.balance)

print("Welcome to the",Customer.bankname)
name=input("Enter the name:- ")
c=Customer(name)
print("Hello {} ,How can I help you?".format(name))
while True:
    print("d-Deposit \nw-Withdraw \ne-Exit")
    print("=========================================")
    print("choose the option:-")
    option=input()
    if option.lower()=="d":
        print("=========================================")
        amount=float(input("Enter the Amount:-"))
        c.deposit(amount)
        print("=========================================")
    elif option.lower()=="w":
        print("=========================================")
        amount=float(input("Enter the Amount:-"))
        c.withdrawl(amount)
        print("=========================================")
    elif(option.lower()=="e"):
        print("=========================================")
        print("Thanks for Banking!!")
        print("=========================================")
        break
    else:
        print("Choose the valid option..")

# output:-
# Welcome to the SBI Bank
# Enter the name:- keadar
# Hello keadar ,How can I help you?
# d-Deposit
# w-Withdraw
# e-Exit
# =========================================
# choose the option:-
# d
# =========================================
# Enter the Amount:-1000000000
# After deposit balance is 1000000000.0
# =========================================
# d-Deposit
# w-Withdraw
# e-Exit
# =========================================
# choose the option:-
# w
# =========================================
# Enter the Amount:-4000000
# After withdrawl balance is 996000000.0
# =========================================
# d-Deposit
# w-Withdraw
# e-Exit
# =========================================
# choose the option:-
# d
# =========================================
# Enter the Amount:-100000000
# After deposit balance is 1096000000.0
# =========================================
# d-Deposit
# w-Withdraw
# e-Exit
# =========================================
# choose the option:-
# w
# =========================================
# Enter the Amount:-98773988
# After withdrawl balance is 997226012.0
# =========================================
# d-Deposit
# w-Withdraw
# e-Exit
# =========================================
# choose the option:-
# e
# =========================================
# Thanks for Banking!!
# =========================================
#
# Process finished with exit code 0

