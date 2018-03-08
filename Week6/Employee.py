from Vehicle import *
from Customer import *


class Employee(object):
    # class variable for employee id
    emp_id = 0

    def __init__(self, name):
        # constructor for employee
        self.__name = name
        self.__id = Employee.emp_id
        Employee.emp_id += 1

    def __str__(self):
        # print output of the object
        return "Employee: " + self.get_name() + " is of type " + self.get_title()

    def get_name(self):
        # getter method for employee name
        return self.__name

    def get_title(self):
        # getter method for employee title
        return "Subordinate"


class Manager(Employee):
    def get_title(self):
        # getter method for manager title
        return "Manager"


    def get_sales_report(self, salesman):
        # method for specific salesman sales report
        # with raise KeyError exception (task 2.d)
        try:
            print(salesman.get_name() + "'s current cumulative sales:")
            print(Salesman.sales[salesman])
        except:
            raise KeyError("Error: This Salesman instance does not have any sales yet.")

    @staticmethod
    def get_sales_report(salesman):
        # method for specific salesman sales report
        # with raise KeyError exception (task 2.d)
        try:
            print(salesman.get_name() + "'s current cumulative sales:")
            print(Salesman.sales[salesman])
        except:
            raise KeyError("Error: This Salesman instance does not have any sales yet.")


class Salesman(Employee):
    # class variable for salesmen sales
    sales = {}

    def sale(self, vehicle, sales_price, customer):
        # method which increments sales dictionary
        if customer.get_score():
            Salesman.sales[self] = Salesman.sales.get(self, 0) + sales_price
        else:
            print("Customer does not have enough credit score")


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

# print(Eric) # expected output: Employee: Eric is of type Manager
# print(Kyle) # expected output: Employee: Kyle is of type Subordinate
# print(Stan) # expected output: Employee: Stan is of type Subordinate
# print(Kenny) # expected output: Employee: Kenny is of type Subordinate
# print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2, 6000, Nimra)

Stan.sale(Veh1,9000,Ahmed)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
