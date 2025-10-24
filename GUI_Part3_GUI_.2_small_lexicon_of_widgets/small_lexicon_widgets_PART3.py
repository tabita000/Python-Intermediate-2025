import tkinter as tk
from tkinter import messagebox

# create the main window
window = tk.Tk()
window.title("Coffee Shop Menu")

# set window size
window.geometry("400x300")

# Create the Menu Bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Variables to store order details
num_coffees = tk.IntVar(value=0)
num_cream = tk.IntVar(value=0)
num_sugar = tk.IntVar(value=0)
num_teas = tk.IntVar(value=0)
num_lemon = tk.IntVar(value=0)
num_honey = tk.IntVar(value=0)

# Donut choice
num_donut_glazed = tk.IntVar(value=0)
num_donut_chocolate = tk.IntVar(value=0)
num_donut_sprinkles = tk.IntVar(value=0)

# Bagel choice
num_bagel_plain = tk.IntVar(value=0)
num_bagel_sesame = tk.IntVar(value=0)
num_bagel_everything = tk.IntVar(value=0)

# prices
PRICE_COFFEE = 2
PRICE_TEA = 2
PRICE_DONUT_CHOCOLATE = 3
PRICE_DONUT_GLAZED = 2.5
PRICE_DONUT_SPRINKLES = 3
PRICE_BAGEL_PLAIN = 2
PRICE_BAGEL_SESAME = 2.5
PRICE_BAGEL_EVERYTHING = 3

# create menu functions
def show_drinks():
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    drinks_frame = tk.Frame(window)
    drinks_frame.pack(padx=10, pady=10)

    tk.Label(drinks_frame, text="Number of Coffees:").grid(row=0, column=0, padx=5, pady=5)
    tk.OptionMenu(drinks_frame, num_coffees, *range(6)).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(drinks_frame, text="Number of Cream:").grid(row=1, column=0, padx=5, pady=5)
    tk.OptionMenu(drinks_frame, num_cream, *range(6)).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(drinks_frame, text="Number of Sugar:").grid(row=2, column=0, padx=5, pady=5)
    tk.OptionMenu(drinks_frame, num_sugar, *range(6)).grid(row=2, column=1, padx=5, pady=5)

    tk.Label(drinks_frame, text="Number of Teas:").grid(row=3, column=0, padx=5, pady=5)
    tk.OptionMenu(drinks_frame, num_teas, *range(6)).grid(row=3, column=1, padx=5, pady=5)

    tk.Label(drinks_frame, text="Number of Lemon:").grid(row=4, column=0, padx=5, pady=5)
    tk.OptionMenu(drinks_frame, num_lemon, *range(6)).grid(row=4, column=1, padx=5, pady=5)

    tk.Label(drinks_frame, text="Number of Honey:").grid(row=5, column=0, padx=5, pady=5)
    tk.OptionMenu(drinks_frame, num_honey, *range(6)).grid(row=5, column=1, padx=5, pady=5)

def show_donuts():
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    donut_frame = tk.Frame(window)
    donut_frame.pack(padx=10, pady=10)

    tk.Label(donut_frame, text="Glazed Donut:").grid(row=0, column=0, padx=5, pady=5)
    tk.OptionMenu(donut_frame, num_donut_glazed, *range(6)).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(donut_frame, text="Chocolate Donut:").grid(row=1, column=0, padx=5, pady=5)
    tk.OptionMenu(donut_frame, num_donut_chocolate, *range(6)).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(donut_frame, text="Sprinkles Donut:").grid(row=2, column=0, padx=5, pady=5)
    tk.OptionMenu(donut_frame, num_donut_sprinkles, *range(6)).grid(row=2, column=1, padx=5, pady=5)

def show_bagel():
    for widget in window.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    bagel_frame = tk.Frame(window)
    bagel_frame.pack(padx=10, pady=10)

    tk.Label(bagel_frame, text="Plain Bagel:").grid(row=0, column=0, padx=5, pady=5)
    tk.OptionMenu(bagel_frame, num_bagel_plain, *range(6)).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(bagel_frame, text="Sesame Bagel:").grid(row=1, column=0, padx=5, pady=5)
    tk.OptionMenu(bagel_frame, num_bagel_sesame, *range(6)).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(bagel_frame, text="Everything Bagel:").grid(row=2, column=0, padx=5, pady=5)
    tk.OptionMenu(bagel_frame, num_bagel_everything, *range(6)).grid(row=2, column=1, padx=5, pady=5)

# Create menus and add to menu bar
drinks_menu = tk.Menu(menu_bar, tearoff=0)
donut_menu = tk.Menu(menu_bar, tearoff=0)
bagel_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Drinks", menu=drinks_menu)
menu_bar.add_cascade(label="Donuts", menu=donut_menu)
menu_bar.add_cascade(label="Bagels", menu=bagel_menu)

# Add menu items and assign commands to the menus
drinks_menu.add_command(label="Show Drinks", command=show_drinks)
donut_menu.add_command(label="Show Donuts", command=show_donuts)
bagel_menu.add_command(label="Show Bagels", command=show_bagel)

# show a page on startup
show_drinks()

# function to display order summary
def show_order_summary():
    total = (
        num_coffees.get() * PRICE_COFFEE +
        num_teas.get() * PRICE_TEA +
        num_donut_glazed.get() * PRICE_DONUT_GLAZED +
        num_donut_chocolate.get() * PRICE_DONUT_CHOCOLATE +
        num_donut_sprinkles.get() * PRICE_DONUT_SPRINKLES +
        num_bagel_plain.get() * PRICE_BAGEL_PLAIN +
        num_bagel_sesame.get() * PRICE_BAGEL_SESAME +
        num_bagel_everything.get() * PRICE_BAGEL_EVERYTHING
    )

    summary = (
        "Order Summary:\n"
        f"Coffees: {num_coffees.get()}  |  Teas: {num_teas.get()}\n"
        f"Glazed Donuts: {num_donut_glazed.get()}\n"
        f"Chocolate Donuts: {num_donut_chocolate.get()}\n"
        f"Sprinkles Donuts: {num_donut_sprinkles.get()}\n"
        f"Plain Bagels: {num_bagel_plain.get()}\n"
        f"Sesame Bagels: {num_bagel_sesame.get()}\n"
        f"Everything Bagels: {num_bagel_everything.get()}\n"
        f"Total Price: ${total:.2f}"
    )

    messagebox.showinfo("Order Summary", summary)

# Create buttons to complete order
complete_order_button = tk.Button(window, text="Complete Order", command=show_order_summary)
complete_order_button.pack(pady=10)

# run
window.mainloop()
