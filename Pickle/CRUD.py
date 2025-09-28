"""
OOP 4.2 - Serialization Using Pickle

This program is an Address Book. It does the followingn
- Keeps peoplees info in a dictionary.
- Lets me Add, Search, Update, and Delete users.
- Saves everything into 'address_book.pkl' using pickle.
- Loads the saved data when the program starts.
"""

import pickle
DATA_FILE = "address_book.pkl"
address_book = {}

def make_key(first_name, last_name):
    return (first_name.strip() + " " + last_name.strip()).lower()

def load_data():
    global address_book
    try:
        with open(DATA_FILE, "rb") as f:
            address_book = pickle.load(f)
        print("Loaded existing address book.")
    except FileNotFoundError:
        address_book = {}
    except Exception as e:
        print("Could not load existing data. Starting empty. Error:", e)
        address_book = {}

def save_data():
    try:
        with open(DATA_FILE, "wb") as f:
            pickle.dump(address_book, f)
        print("Changes saved.")
    except Exception as e:
        print("Save failed:", e)

def add_user():
    print("\n--- Add New User ---")
    first = input("Enter first name: ").strip()
    last = input("Enter last name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    key = make_key(first, last)
    if key in address_book:
        print("That person already exists. Use Change Existing User instead.")
        return

    address_book[key] = {"first": first, "last": last, "phone": phone, "email": email}
    save_data()
    print("User added.")

def search_user():
    print("\n--- Search for Existing User ---")
    first = input("Enter first name: ").strip()
    last = input("Enter last name: ").strip()
    key = make_key(first, last)

    if key in address_book:
        user = address_book[key]
        print("User found:")
        print("First Name:", user["first"])
        print("Last Name: ", user["last"])
        print("Phone:     ", user["phone"])
        print("Email:     ", user["email"])
    else:
        print("User not found.")

def change_user():
    print("\n--- Change Existing User ---")
    first = input("Enter current first name: ").strip()
    last = input("Enter current last name: ").strip()
    key = make_key(first, last)

    if key not in address_book:
        print("User not found.")
        return

    current = address_book[key]
    print("Enter new details (press Enter to keep the old value):")

    new_first = input("First name [" + current["first"] + "]: ").strip() or current["first"]
    new_last  = input("Last name  [" + current["last"] + "]: ").strip() or current["last"]
    new_phone = input("Phone      [" + current["phone"] + "]: ").strip() or current["phone"]
    new_email = input("Email      [" + current["email"] + "]: ").strip() or current["email"]

    new_key = make_key(new_first, new_last)
    del address_book[key]
    address_book[new_key] = {"first": new_first, "last": new_last, "phone": new_phone, "email": new_email}
    save_data()
    print("User updated.")

def delete_user():
    print("\n--- Delete Existing User ---")
    first = input("Enter first name: ").strip()
    last = input("Enter last name: ").strip()
    key = make_key(first, last)

    if key in address_book:
        confirm = input("Are you sure you want to delete " + first + " " + last + "? (y/n): ").strip().lower()
        if confirm == "y":
            del address_book[key]
            save_data()
            print("User deleted.")
        else:
            print("Delete canceled.")
    else:
        print("User not found.")

def show_menu():
    print("\nAddress Book Menu:")
    print("1. Add New User")
    print("2. Search for Existing User")
    print("3. Change Existing User")
    print("4. Delete Existing User")
    print("5. Exit")

def main():
    load_data()
    running = True
    while running:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            search_user()
        elif choice == "3":
            change_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Goodbye!")
            running = False
        else:
            print("Please enter a valid choice (1-5).")

if __name__ == "__main__":
    main()