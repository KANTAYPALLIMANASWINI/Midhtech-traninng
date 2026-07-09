# class BankAccount:                               # Create a class

#     def __init__(self, owner, balance):          # Constructor
#         self.owner = owner                       # Public variable
#         self.__balance = balance                 # Private variable

#     def show_balance(self):                      # Public method
#         print("Owner:", self.owner)              # Access public variable
#         print("Balance:", self.__balance)        # Access private variable inside the class

# account1 = BankAccount("Ravi", 5000)             # Create an object

# account1.show_balance()                          # Call the public method


###another example
class BankAccount:
    def  __init__(self,owner,balance):
        self.owner=owner
        self._account_type="Savings"
        self._balance=balance
    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
    def withdraw(self,amount):
        if 0<amount<=self._balance:
            self._balance-=amount
            print("Withdraw Successfull")
        else:
            print("Insufficient balance or invalid amount")
    def show_balance(self):
        print("Balance:",self._balance)

account=BankAccount("john",1000)
print("owner:",account.owner)
print("Account type:",account._account_type)

account.deposit(500)
account.withdraw(300)
account.show_balance()


            