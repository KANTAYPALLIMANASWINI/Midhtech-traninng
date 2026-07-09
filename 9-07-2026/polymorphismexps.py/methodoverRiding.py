# Method Overriding Example

class Bank:

    def interest(self):
        print("Interest Rate: 5%")

class SBI(Bank):

    def interest(self):
        print("Interest Rate: 7%")

obj = SBI()

obj.interest()