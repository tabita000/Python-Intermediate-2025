from Car import Car

#test direct attribute
my_car = Car("Toyota", "Highlander", 18, 5)
print("Direct access changed _make to:" , my_car._make)

#test getter and setter
my_car.make = "Honda"
print("Getter returns make:", my_car.make)

#test method functionality
my_car.add_gas(10) #add gas through method
print("Car info after adding gas:", my_car.car_info()) #shows all car details