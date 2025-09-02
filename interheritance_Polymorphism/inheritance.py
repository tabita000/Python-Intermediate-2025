class Dog:
    def __init__(self, average_weight, height_range, life_span, color):
        self.average_weight = average_weight
        self.height_range = height_range
        self.life_span = life_span
        self.color = color
        
class HoundDog(Dog):
    def __init__(self, average_weight, height_range, life_span, color, scent_level):
        super().__init__(average_weight, height_range, life_span, color)  
        self.scent_level = scent_level #added attribute
        
    def track(self):
        return "This dog is tracking a scent!"   #method
    
    
class DogToy(Dog):
    def __init__(self, average_weight, height_range, life_span, color, cuddle_level):
        super().__init__(average_weight, height_range, life_span, color)  
        self.cuddle_level = cuddle_level #added attribute 
        
    def cuddle(self):  #method
        return "This dog loves cuddles!"
    
    
    
if __name__ == "__main__":
    
    beagle = HoundDog(25, "13-15 inches", "12-15 years", "tri-color", "height")
    print(f"Beagle: {beagle.track()}")
    
    chihuahua = DogToy(6, "5-8 inches", "14-16 years", "brown", "super")
    print(f"Chihuahua: {chihuahua.cuddle()}")
    
                