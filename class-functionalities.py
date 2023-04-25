class Vehicle:
    no_of_cars = 0                                            #class variable
    def __init__(self, vendor, category):                     #constructor
        self.vendor = vendor
        self.category = category
        Vehicle.no_of_cars += 1

    def carDetail(self):                                       #method
        return self.vendor, self.brand                         #instance variable

    @classmethod
    def makeVehicle(cls, vehicle):
        vendor, category = vehicle.split("-")
        return cls(vendor, category)

    @staticmethod
    def buyMe():
        return "Get rich to buy me ;)"

car_1 = Vehicle('audi', 'luxury')                            
car_2 = Vehicle('bmw', 'luxury')
veh_str = 'lamborghini-luxurysports'
car_3 = Vehicle.makeVehicle(veh_str)
print(car_3.buyMe())
# print(Vehicle.brand)
# print(Vehicle.__dict__)
# print(car_2.__dict__)
# print(car_3.carDetail())
# print(Vehicle.buyMe())
