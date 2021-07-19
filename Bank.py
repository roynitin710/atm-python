class Bank:

    def create_pin(self):
        self.pin = input("Create your 4 digit pin")
        self.balance = int(input("Deposit your first amount"))
        print("Congrats your account has been created")
        self.user_menu()

    def user_menu(self):
        user_input = input("""
        Hi there! how would you like to proceed?
        1. Create pin
        2. Withdraw
        3. Deposit
        4. Check balance
        5. Change pin
        6. Anything else to exit
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.withdraw()
        elif user_input == "3":
            self.deposit()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.change_pin()
        else:
            exit(0)

    def withdraw(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            amount = int(input("Enter the amount needed"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Amount withdrawn successfully")
            else:
                print("Hatt be")
        else:
            print("Incorrect Pin")
        self.user_menu()

    def deposit(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            amount = int(input("Enter the amount to be deposited"))
            self.balance = self.balance + amount
            print("Amount deposited successfully")
        else:
            print("Incorrect Pin")

        self.user_menu()

    def check_balance(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            print(self.balance)
        else:
            print("Incorrect pin")

        self.user_menu()

    def change_pin(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            self.pin = input("Enter new pin")
            print("Pin change successful")
        else:
            print("Incorrect pin")

        self.user_menu()


rahul = Bank()

rahul.user_menu()