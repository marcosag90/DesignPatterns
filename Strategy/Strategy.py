'''
    We will create a context. This will be a class that will simulate a shopping
    cart, and we will accept payments vis Credit Card, Cash, and PayPal.
    Please, note that we are not coding very safely here. This example is just
    meant to illustrate the behavior of the strategy pattern
'''
from abc import ABC, abstractmethod
class ShoppingCart(object):
    def __init__(self):
        self.items = []
        self.paymentMethod = None

    def addItem(self, item):
        self.items.append(item)

    def calculateTotal(self):
        total = 0
        for item in self.items:
            total += item.getPrice()
        return total

    def setPaymentMethod(self, method):
        if(isinstance(method, PaymentStrategy)):
            self.paymentMethod = method
        else:
            raise TypeError("The method that you passed is not a PaymentStrategy")


    def pay(self):
        self.paymentMethod.pay(self.calculateTotal())




'''
    We will create a small class for the items...
'''
class item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def getPrice(self):
        return self.price
    



''' 
    Let's go now with the pool of strategies. First, we create the interface, then 
    we derive all the strategies from that method.
'''

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print("Paying $", amount, " via Credit Card")
        # code to process a credit card payment

class CashStrategy(PaymentStrategy):
    def pay(self, amount):
        print("Paying $", amount, " in cash")
        # code to register the payment in cash somewhere

class PayPalStrategy(PaymentStrategy):
    def pay(self, amount):
        print("Paying $", amount, "via Paypal.")
        # code to perform a payment via paypal



'''
    Lets create now the test program
'''

if(__name__ == "__main__"):
    # Register our products
    rice = item("rice", 1.5)
    chocolate = item("choclate", 2.3)
    milk = item("milk", 0.7)
    cheese = item("cheese", 3.2)

    # not very interactive here
    customer = ShoppingCart()
    payment = None
    option = None
    while(option != '5'):
        print("Current Total: $", customer.calculateTotal())
        option = input("Select an item: 1) rice, 2) chocolate, 3) milk, 4) cheese, 5) pay & exit: ")
        if(option == '1'):
            print('Added rice')
            customer.addItem(rice)
        elif(option == '2'):
            print('Added chocolate')
            customer.addItem(chocolate)
        elif(option == '3'):
            print('Added milk')
            customer.addItem(milk)
        elif(option == '4'):
            print('Added cheese')
            customer.addItem(cheese)
        elif(option == '5'):
            print("Select a payment method:")
            while(payment not in ['1', '2', '3']):
                payment = input("1) cash, 2) credit card, 3) paypal: ")
                if(payment == '1'):
                    customer.setPaymentMethod(CashStrategy())
                elif(payment == '2'):
                    customer.setPaymentMethod(CreditCardStrategy())
                elif(payment == '3'):
                    customer.setPaymentMethod(PayPalStrategy())
                else:
                    print("Please, select a valid payment method")
        else:
            print("Please enter a valid value") 
    # Pay
    customer.pay()
    print("Have a good one!!")

    #customer.setPaymentMethod(1)
    