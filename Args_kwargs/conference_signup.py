# #*args — many things, no labels
# def potluck(*dishes):
#     print("Dishes that arrived:")
#     for d in dishes:
#         print("-", d)

# potluck("pizza", "salad", "brownies")
# print(" \n")

# #**kwargs — many things, with labels
# def labeled_potluck(**labels):
#     print("Labels people gave:")
#     for name, value in labels.items(): #labels.items() means: give me the pairs from this dictionary.
#         print(f"{name} = {value}")
        
# labeled_potluck(vegan=True, gluten_free=False, drink="Soda")
# print(" \n")

# labels = {"vegan": True, "drinks": "soda", "guests": 12}

# print(list(labels.keys()))
# print(list(labels.values()))
# print(list(labels.items()))

# print(" \n")
# Labels people gave:
# vegan = True
# gluten_free = False
# drinks = soda


#USING BOTH TOGETHER
# def party(host, *dishes, **notes):
#     print("Host:", host)
#     print("Dishes:")
#     for d in dishes:
#         print("-", d)
#     print("Notes:")
#     for k, v in notes.items():
#         print(f"{k} = {v}")

# party(
#     "Tabita",                     # host (regular arg)
#     "pizza", "salad", "cookies",  # *args (unnamed extra)
#     vegan=True, drinks="soda"     # **kwargs (named extra)
# )

def conference_signup(*participants, **contacts):
    print("Conference participants and their details: ")
    print("--------------------------------------------")
    
    #if there aren't any participants
    if not participants:
        print("No participants added yet.")
        print("--------------------------------------------")
        return
        
    for name in participants:
        email, phone = contacts.get(name)
        if email is None: email = "N/A"
        if phone is None: phone = "N/A"


        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print("--------------------------------------------")
        
        
attendees = ("Alice", "Bob", "Charlie")
details = {
    "Alice": ("alice@example.com", "123-456-7890"),
    "Bob": ("bob@example.com", "987-654-3210"),
    "Charlie": ("charlie@example.com", None),  # missing phone
}  

conference_signup(*attendees, **details)      