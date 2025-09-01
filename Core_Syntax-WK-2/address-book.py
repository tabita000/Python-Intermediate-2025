a = 10 + 5 # 15
b = 10 - 5 # 5
c = 4 * 3 # 12
d = 9 / 2 # 4.5
e = 10 % 3 # 1

#Rational operators
print(5 == 5) #True
print (5 != 3) #True
print (7 > 2) #True
print (6 >= 6) #True
print (2 <= 3) #True

#List Functions
nums = [1,2,3]
nums.append(4)
nums.remove(2)
last = nums.pop() #remove last item in list
print (nums)

#Built in functions
print("Hello")
print(type(42)) #int
print(len("Hello")) #5

"""
        MY NOTES:
        - Use setter and getter. 
        - Without a setter, someone could set a.first_name = "" or a.zip = "ABC" and Python would not care. 
        - With a setter, you can validate and either fix, block, or warn about bad data before it sneaks into your object. 
        - Setter = data safety / validation. 
        - An underscore `_` in front of an attribute means it's treated as private (should not be accessed directly). 
        - The private variable stores the user input safely. 
        - The setter decides if the new input is valid. If it's not (like empty), show a validation message instead of saving it.
        
        **getter = give me what’s inside

        setter = put this new thing inside (but don’t allow empty)**
        
"""


 # 'magic' or 'dunder' method . Dunder is "Double Underscore"

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        
    def __str__(self):
        return f"Book: {self.title}"
    
    def __repr__(self):
        return f"Book(title={self.title}, pages={self.pages})"
    

b = Book("Python", 100)  
print(b)  


"""
class to represent an address book entry.
Attributes include attribute details
Methods include methods details
"""
class AddressBook:
    def __init__(self,first_name, last_name, birthday, email, street_name, city, state, zip, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.street_name = street_name
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        
        """
        MY NOTES:
        - Use setter and getter. 
        - Without a setter, someone could set a.first_name = "" or a.zip = "ABC" and Python would not care. 
        - With a setter, you can validate and either fix, block, or warn about bad data before it sneaks into your object. 
        - Setter = data safety / validation. 
        - An underscore `_` in front of an attribute means it's treated as private (should not be accessed directly). 
        - The private variable stores the user input safely. 
        - The setter decides if the new input is valid. If it's not (like empty), show a validation message instead of saving it.
        
        **getter = give me what’s inside

        setter = put this new thing inside (but don’t allow empty)**
        
        """
        #FIRST NAME
    def get_first_name(self): #getter
        return self.first_name
    
    def set_first_name(self, user_input_first_name): #setter
        if not user_input_first_name:
            raise ValueError("First name cannot be empty")
        self.first_name = user_input_first_name
            
    #LAST NAME
    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, user_input_last_name):
        if not user_input_last_name:
            raise ValueError("Last name cannot be empty")
        self.last_name = user_input_last_name
        
    #BIRTHDAY
    def get_birthday(self):
        return self.birthday
    
    def set_birthday(self, user_birthday):
        if not user_birthday:
            raise ValueError("Birthday cannot be empty")
        self.birthday = user_birthday
        
    #EMAIL
    def get_email(self):
        return self.email
    
    def set_email(self, user_email):
        if not user_email:
            raise ValueError ("Email cannot be empty")
        self.email = user_email
        
    #STREET ADDRESS
    def get_street_name(self):
        return self.street_name
    
    def set_street_name(self, user_street_name):
        if not user_street_name:
            raise ValueError("Street name cannot be empty")
        self.street_name = user_street_name
        
    #CITY
    def get_city_name(self):
        return self.city
    def set_city_name(self, user_city_name):
        if not user_city_name:
            raise ValueError("City cannot be empty")
        self.city = user_city_name

    #STATE
    def get_state_name(self):
        return self.state
    def set_state_name(self, user_state_name):
        if not user_state_name:
            raise ValueError("State cannot be empty")
        self.state = user_state_name
        
    #ZIP CODE
    def get_zip(self):
        return self.zip
    
    def set_zip(self, user_zip):
        if not user_zip:
            raise ValueError("Zip code cannot be empty")
        self.zip = user_zip
        
    #PHONE
    def get_phone(self):
        return self.phone
    def set_phone(self, user_phone):
        if not user_phone:
            raise ValueError("Phone cannot be empty")
        self.phone = user_phone 
        
        
    #MAGIC METHOD
    def __str__(self):
        return (
            f"First Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Birthday: {self.birthday}\n"
            f"Email: {self.email}\n"
            f"Street Address: {self.street_name}\n"
            f"City: {self.city}\n"
            f"State: {self.state}\n"
            f"Zip Code:{self.zip}\n"
            f"Phone: {self.phone}\n"
        )
        
        
    #ID TAG FOR DEBUGGING. IS USED BY PYHTON/DEV TOOLS
    def __repr__(self):
        #short debug text
        return f"AddressBook(first_name={self.first_name!r}, last_name={self.last_name!r}, email={self.email!r})"
    
    def __eq__(self, other_entry):
        if not isinstance(other_entry, AddressBook):
            return NotImplemented
        #treating email like a unique ID
        return self.email == other_entry.email
    
    
                      
p1 = AddressBook("Suniana", "Albert", "06/19/1994", "suniana.albert@example.com",
                 "583 Glenn Ridge", "Crystal Lake", "IL", "60014", "847-533-9516")
p2 = AddressBook("Shawn", "Sadiq", "08/14/1991", "shawn.sadiq@example.com",
                 "421 Lakeview Crossing Apt 2B", "Schaumburg", "IL", "60193", "(312) 555-0178")

p3 = AddressBook("Sana", "Gohar", "03/05/1993", "sana.gohar@example.com",
                 "9804 Meadowlark Court", "Plano", "TX", "75025", "(469) 555-0136")

p4 = AddressBook("Ayesha", "Khan", "12/11/1990", "ayesha.khan@example.com",
                 "730 Brookside Lane Unit 4C", "Naperville", "IL", "60540", "(630) 555-0191")

people = [p1, p2, p3, p4]

#loop through list, uses __str__
for person in people:
    print(person)
    print()