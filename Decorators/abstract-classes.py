# OOP 2.6 – Abstract Classes
# Bakery Example: Abstract class and two child classes

"""
Abstract class (BakedGood) is the blueprint.
Abstract methods (add_in, description) force child classes to provide
their own version.
Croissant and Muffin are child classes. They implement add_in() and
description()
"""

from abc import ABC, abstractmethod

#Abstract Class
class BakedGood(ABC):
    def __init__(self, size, flavor):
        self.size = size
        self.flavor = flavor

    @abstractmethod
    def add_in(self):
        pass

    @abstractmethod
    def description(self):
        pass


#Child Class
class Croissant(BakedGood):
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def add_in(self):
        return "Almonds"

    def description(self):
        return f"Croissant: {self.size}, {self.flavor}, with {self.add_in()}"


#Child Class
class Muffin(BakedGood):
    def __init__(self, size, flavor):
        super().__init__(size, flavor)

    def add_in(self):
        return "Blueberries"

    def description(self):
        return f"Muffin: {self.size}, {self.flavor}, with {self.add_in()}"


#testing
croissant = Croissant("Large", "Butter")
print(croissant.description())   

muffin = Muffin("Medium", "Chocolate")
print(muffin.description()) 


                                           #EXAMPLE FROM MODULE
class Drink(ABC):  #parent abstract class
    @abstractmethod
    def __init__(self, size, milk_type):
        self.size = size
        self.milk_type = milk_type
        
    @abstractmethod
    def add_in(self):
        pass
    
    @abstractmethod
    def description(self):
        pass
    
class LondonFog(Drink): #child class 1
    def add_in(self):
        return "Vanilla Syrup" 
    def description(self):
        return f"London fog: {self.size}, {self.milk_type} milk, with {self.add_in()}"
    
class MatchaTeaLatte(Drink):  #child class 2
    def add_in(self):
        return "Honey"
    def description(self):
        return f"Matcha Tea Latte: {self.size}, {self.milk_type} milk, with {self.add_in}"
             
        
 


