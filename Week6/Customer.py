from Vehicle import *
import random


class Customer(object):
    def __init__(self, name):
        # constructor for Customer
        self.__name = name
        self.__score = self.credit_score()

    def __str__(self):
        # print output of the object
        return "Customer: " + self.__name

    def credit_score(self):
        # generating credit score
        score = random.randint(0, 100)
        if score > 60:
            return True
        else:
            return False

    def get_score(self):
        # getter for the score
        return self.__score


class VIP_Customer(Customer):
    def credit_score(self):
        # generating credit score
        return True


### test cases ###


Nimra = Customer("Nimra")
Ahmed = VIP_Customer("Ahmed")

print(Nimra)
print(Ahmed)

print(Nimra.get_score())
print(Ahmed.get_score())
