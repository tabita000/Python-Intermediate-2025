# importing tkinter
import tkinter as tk
from tkinter import messagebox

# creating the main window
window = tk.Tk()
window.title("Data Entry Form")
 
 
# using frames for organization
frame_entry = tk.Frame(window)
frame_buttons = tk.Frame(window)

# place the frames in the window using grid layout
frame_entry.grid(row=0, column=0, padx=10, pady=10)
frame_buttons.grid(row=1, column=0, padx=10, pady=10) 

        # adding entry fields and labels
# name entry
label_name = tk.Label(frame_entry, text="Name:")
entry_name = tk.Entry(frame_entry)

label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# email entry
label_email = tk.Label(frame_entry, text="Email:")
entry_email = tk.Entry(frame_entry)

label_email.grid(row=1, column=0, padx=5, pady=5)
entry_email.grid(row=1, column=1, padx=5, pady=5)

# phone entry
label_phone = tk.Label(frame_entry, text="Phone:")
entry_phone = tk.Entry(frame_entry) 

label_phone.grid(row=2, column=0, padx=5, pady=5)
entry_phone.grid(row=2, column=1, padx=5, pady=5)

# address entry
label_address = tk.Label(frame_entry, text="Address:")
entry_address = tk.Entry(frame_entry)

label_address.grid(row=3, column=0, padx=5, pady=5)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# phone type checkboxes
label_phone_type = tk.Label(frame_entry, text="Phone Type:")
phone_type_var = tk.StringVar()
checkbox_home = tk.Checkbutton(frame_entry, text="Home", variable=phone_type_var, onvalue="Home")
checkbox_mobile = tk.Checkbutton(frame_entry, text="Mobile", variable=phone_type_var, onvalue="Mobile")

label_phone_type.grid(row=4, column=0, padx=5, pady=5)
checkbox_home.grid(row=4, column=1, padx=5, pady=5, sticky='w')
checkbox_mobile.grid(row=5, column=1, padx=5, pady=5, sticky='w')
        
        # adding buttons
# function to display the entered information
def display_info():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    phone_type = phone_type_var.get()
    address = entry_address.get()
    
    info = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\nPhone Type: {phone_type}"             

# add buttons
button_display = tk.Button(frame_buttons, text="Display Info", command=display_info)
button_quit = tk.Button(frame_buttons, text="Quit", command=window.destroy)

button_display.grid(row=0, column=0, padx=10, pady=10)
button_quit.grid(row=0, column=1, padx=10, pady=10)


# run
window.mainloop()
