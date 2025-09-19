# smart_home.py
# OOP 2.8 – Composition vs Inheritance

"""
This program is a smart home system that shows how inheritance and composition work. 
Device is the base class, and Light and Thermostat inherit from it. LEDLight and SmartBulb 
inherit from Light. The SmartHome class uses composition because it has all the devices inside it. 
The program gives a menu where you can turn devices on or off, change brightness, or set the 
thermostat temperature until you exit.
"""

# base class with methods
class Device:
    def __init__(self, name, is_on=False):
        self.name = name
        self.is_on = is_on
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def status_text(self):
        return "On" if self.is_on else "Off"   
    
    
# light class
class Light(Device):
    def __init__(self, name, is_on=False, brightness=100):
        super().__init__(name, is_on) # inherited name and is_on
        self.brightness = self._clamp(brightness) 
        
    def set_brightness(self, value):
        try:
            value = int(value)
        except:
            value = 100
        self.brightness = self._clamp(value)
        
    def _clamp(self, v):
        if v < 0:
            return 0
        elif v > 100:
            return 100
        else: 
            return v
        
    def info(self):
        return f"{self.name} - Status: {self.status_text()}, Brightness: {self.brightness}%"  
    
    
class LEDLight(Light):
    def __init__(self, name, is_on=False, brightness=100):
        super().__init__(name, is_on, brightness)
        
    def info(self):
        return f"{self.name} (LED) - Status: {self.status_text()}, Brightness: {self.brightness}%"
    
    
class SmartBulb(Light):
    def __init__(self, name, is_on=False, brightness=100):
        super().__init__(name, is_on, brightness)
        
    def info(self):
        return f"{self.name} (Smart Bulb) - Status: {self.status_text()}"
    
    
#thermostat
class Thermostat(Device):
    def __init__(self, name, is_on=False, current_temp=72.0, target_temp=68.0):
        super().__init__(name, is_on)
        self.current_temp = float(current_temp)
        self.target_temp = self._clamp_target(target_temp)    
        
    def set_target_temp(self, value):
        try:
            value = float(value)
        except:
            value = self.target_temp
        self.target_temp = self._clamp_target(value)
        
    def _clamp_target(self, value):
        if value < 50:
            return 50
        elif value > 90:
            return 90
        else:
            return value
        
    def info(self):
        return(f"{self.name} - Status: {self.status_text()}," f"Current Temperature: {self.current_temp:.0f} Fahrenheit, " 
        f"Target Temperature: {self.target_temp:.0f} Fahrenheit")
        
#SmartHome-Composotion
class SmartHome:
    def __init__(self):
        #SmartHome devices
        self.led = LEDLight("LED Light", True, 75) #will start ON
        self.bulb = SmartBulb("Smart Bulb") #starts off
        self.thermo = Thermostat("Thermostat", True, 72, 68) #starts on
        self.devices = [self.led, self.bulb,self.thermo]
        
    def print_devices(self):
        print("\nDevices:")
        i = 1
        for d in self.devices:
            print(f"{i}. {d.info()}")
            i += 1
            
    def main_loop(self):
        while True:
            print("\n====Smart Home System====")
            self.print_devices()
            print("\nMain Menu:")
            print("1) Select a device to control")
            print("2) Exit program")
            choice = input("Enter your choice (1-2): ").strip()
         
            if choice == "1":
                self.select_device_menu()
            elif choice == "2":
                print("Exiting Smart Home. Goodbye!")
                break
            else:
                print("Please enter 1 or 2.")
                
    def select_device_menu(self):
        sel = input("\n enter the number of the device you want to control (or 0 to go back): ").strip()
        if not sel.isdigit():
            print("Please enter a valid number.")
            return
        sel = int(sel)
        if sel == 0:
            return
        if sel < 1 or sel > len(self.devices):
            print("Invalid device number")
            return
        device = self.devices[sel - 1]
        if isinstance(device, Light):
            self.light_menu(device)
        elif isinstance(device, Thermostat):
            self.thermostat_menu(device)
        else:
            self.device_menu(device)
            
    def device_menu(self, device):
        while True:
            print(f"\n[{device.name}] - {device.info()}")
            print("1) Turn device ON")
            print("2) Turn device OFF")
            print("3) Return to main menu")
            c = input("Select an option (1-3): ").strip()
            if c == "1":
                device.turn_on()
                print(f"{device.name} is now ON.")
            elif c == "2":
                device.turn_off()
                print(f"{device.name} is now OFF.")
            elif c == "3":
                return
            else:
                print("Please enter 1–3.")  
            
    def light_menu(self, light):
        while True:
            print(f"\n[{light.name}] – {light.info()}")
            print(f"1) Turn {light.name} ON")
            print(f"2) Turn {light.name} OFF")
            print(f"3) Set {light.name} Brightness (0–100)")
            print("4) Return to main menu")
            c = input(f"Select an option for {light.name} (1–4): ").strip()
            if c == "1":
                light.turn_on()
                print(f"{light.name} is now ON.")
            elif c == "2":
                light.turn_off()
                print(f"{light.name} is now OFF.")
            elif c == "3":
                val = input(f"Enter new brightness for {light.name} (0–100): ").strip()
                light.set_brightness(val)
                print(f"{light.name} brightness set to {light.brightness}%.")
            elif c == "4":
                return
            else:
                print("Please enter 1–4.")

    def thermostat_menu(self, t):
        while True:
            print(f"\n[{t.name}] – {t.info()}")
            print(f"1) Turn {t.name} ON")
            print(f"2) Turn {t.name} OFF")
            print(f"3) Set {t.name} Target Temperature (50–90 Fahrenheit)")
            print("4) Return to main menu")
            c = input(f"Select an option for {t.name} (1–4): ").strip()
            if c == "1":
                t.turn_on()
                print(f"{t.name} is now ON.")
            elif c == "2":
                t.turn_off()
                print(f"{t.name} is now OFF.")
            elif c == "3":
                temp = input("Enter new target temperature (50–90Fahrenheit): ").strip()
                t.set_target_temp(temp)
                print(f"{t.name} target temperature set to {t.target_temp:.0f}Fahrenheit.")
            elif c == "4":
                return
            else:
                print("Please enter 1–4.")


#Run program
if __name__ == "__main__":
    SmartHome().main_loop()  




#CLASS LECTURE EXAMPLES
            
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def eat(self):
#         return f"{self.name} is eating."

# class Dog(Animal): 
    
#     def bark(self):
#         return "Woof!"


# class Zoo:
#     def __init__(self):
#         self.animal = []
#     def add(self, animal):
#         self.animal.append(animal)
        
# dog1 = Dog("Buddy")
# print(dog1.eat())
# print(dog1.bark())

# z = Zoo()
# dog1 = Dog("Jackie")
# dog2 = Dog("Charlie")
# dog3 = Dog("Zues")

# z.add(dog1)
# z.add(dog2)
# z.add(dog3)

# for member in z.animal:
#     print(member.name)