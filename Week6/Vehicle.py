import sys


class Vehicle(object):
    # class variable for id
    vehicle_id = 0

    # class variable for list of vehicles sold
    vehicles_sold = []

    def __init__(self, year, mileage, purchase_price, serial_number):
        # constructor for Vehicle
        self.__vehicle_id = Vehicle.generate_vehicle_id()
        Vehicle.vehicle_id += 1

        self.__serial_number = serial_number

        # handling exception (task 2.d)
        try:
            self.__year = int(year)
            self.__mileage = int(mileage)
            self.__purchase_price = int(purchase_price)
        except ValueError:
            print("Error: Year, Mileage and Price must be integers")
            sys.exit()

    def __str__(self):
        # print output of the object
        veh_id = self.get_id()
        return "\t{0:d}".format(veh_id)

    def get_id(self):
        # getter for id
        return self.__vehicle_id

    @staticmethod
    def generate_vehicle_id():
        # generating vehicle id
        return 100000 + Vehicle.vehicle_id


class Car(Vehicle):
    def __init__(self, year, mileage, purchase_price, serial_number, doors):
        # constructor for Car
        Vehicle.__init__(self, year, mileage, purchase_price, serial_number)

        self.__doors = doors
        self.__wheels = 4


class Lorry(Vehicle):
    def __init__(self, year, mileage, purchase_price, serial_number, wheels, doors=2):
        # constructor for Lorry
        Vehicle.__init__(self, year, mileage, purchase_price, serial_number)
        self.__doors = doors
        self.__wheels = wheels


class Motorcycle(Vehicle):
    # class variable for classic count
    classic_count = 0

    def __init__(self, year, mileage, purchase_price, serial_number, classic=False):
        # constructor for Motorcycle
        Vehicle.__init__(self, year, mileage, purchase_price, serial_number)
        self.__wheels = 2
        self.__classic = classic

        # incrementing for every classic motorcycle
        if self.__classic == True:
            Motorcycle.classic_count += 1


### test cases ###

# initialising vehicle instances

Veh1 = Vehicle(2008, 65000, 7500, "34567851g4")
Veh2 = Car(2007, 125000, 5500, "e44653ftu1", 4)
Veh3 = Car(2012, 45000, 8900, "gf5622iguz", doors=2)
Veh4 = Lorry(2005, 180000, 16000, "hbh997123f", 6)
Veh5 = Lorry(2013, 30000, 35000, "hjbf17jbkh", 8, 4)
Veh6 = Motorcycle(1975, 75500, 40000, "bh545664rh", True)
veh_list = [Veh1, Veh2, Veh3, Veh4, Veh5, Veh6]

for veh in veh_list:
    print(veh)