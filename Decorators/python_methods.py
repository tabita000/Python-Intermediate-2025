# OOP 2.5 — Different Faces of Python Methods
# Example class: Duck
# Shows: instance methods, class methods, static methods
"""
Cheat sheet:

Instance method → first parameter is self → uses/changes that one object’s data.

Class method → first parameter is cls → changes class-level stuff for all objects.

Static method → no self, no cls → just a helper function that fits the class topic.
"""

class Duck:
    species = "bird"
    #create each duck- instance variable
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        #instance method
    def quack(self):
        return f"{self.name} says quack!" 
    def birthday(self):
        self.age += 1
        return f"{self.name} is {self.age} years old"
    
duck1 = Duck("Daffy", 3)
duck2 = Duck("Donald", 5)
print(duck1.quack())
print(duck2.quack()) 
print(duck1.birthday())
print(duck2.birthday())   


#class method
class Duck:
    species = "bird"
    
    def __init__(self,name):
        self.name = name
    @classmethod    
    def set_species(cls, species):
        cls.species = species
        
print("Original species: ",Duck.species)  
Duck.set_species("Waterfowl")
print("New Species: ", Duck.species)  

#static method
class Duck:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def fly(distance):
        return f"Ducks can fly {distance} miles without stopping."
    
print(Duck.fly(15))
              
    
    
    
#   DIFFERENT FACES OF PYTHON METHODS:  Examples from module

#   Instance Method
# class Duck:
#     def __init__(self, name):
#         self.name = name
        
#     def quack(self):
#             return f'{self.name} says quack!'
#     #Creating an instance of Duck
# duck = Duck('Daffy')
# print(duck.quack())
# print("")


#    Class Method
# class Duck:
#     species = "bird"
#     def __init__(self, name):
#          self.name = name
         
#     @classmethod
#     def set_species(cls, species):
#         cls.species = species  
#        # changing the class attribute "species" for all instances 
# Duck.set_species("Waterfowl")
# print(Duck.species) 
# print("")  

    #Static Method
# class Duck:
#     def __init__(self, name):
#          self.name = name
         
#     @staticmethod
#     def fly():
#         return "Ducks can fly!" 
        # calling a static method
# print(Duck.fly())