class ToyCar:
    
    toy_type = "car" #class variable
    
    def __init__(self, brand, color, car_type, motorized): #attributes
        self.brand = brand  #Instance Variables
        self.color = color
        self.car_type = car_type
        self.motorized = motorized
        
     #Methods 👇🏼
    def paly(self):
        print("The toy car moves forwrad")    
        
    def sound(self):
        print("Vroom")
        
        
#Instances(objects)
race_car = ToyCar("Hot Wheels", "White", "race car", True)
pickup_truck = ToyCar("Tonka", "yellow", "pickup truck", False)
police_car = ToyCar("Matchbox", "blue", "police car", True)

#class of each instance
print(race_car.__class__)
print(pickup_truck.__class__)
print(police_car.__class__)

# Dictionary of one instance
print(race_car.__dict__)

race_car.paly()
race_car.sound()