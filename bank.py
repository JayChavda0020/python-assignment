class Bank:
    def open_account(self, acno, cname, balance):
        self.acno = acno
        self.cname = cname
        self.balance = balance
        print("Hello", self.cname, "Your Account Number", self.acno, "Is Opened With", self.balance, "Rs.")

    def deposit(self, amount):
        self.balance += amount
    
    def withdrwal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Sorry You Need Another", amount - self.balance, "Rs.")

    def check_balance(self):
        print("Your Current Balance Is : ", self.balance, "Rs.")

b1 = Bank()
acno = int(input("Enter Account Number : "))
cname = input("Enter Customer Name : ")
balance = int(input("Enter Initial Balance : "))

b1.open_account(acno, cname, balance)

while True:
    print("*"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*50)

    choice = (int(input("Enter Your Choice : ")))
    print("*"*50)

    if choice == 1:
        amount = int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*50)

    elif choice == 2:
        amount = int(input("Enter Withdrawl Amount : "))
        b1.withdrwal(amount)
        print("*"*50)

    elif choice == 3:
        b1.check_balance()
        print("*"*50)

    elif choice == 4:
        print("Thank You For Using Our Service")
        print("*"*50)
        break
    else:
        print("Invalid Choice, Please Try Again")