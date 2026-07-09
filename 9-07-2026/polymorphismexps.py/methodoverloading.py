# Method Overloading Example

class Shopping:

    def bill(self, price1, price2=0):
        print("Total Bill:", price1 + price2)

obj = Shopping()

obj.bill(500)
obj.bill(500, 1000)