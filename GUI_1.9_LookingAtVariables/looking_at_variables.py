# GUI 1.9 Using Observable Variables in Tkinter
import tkinter as tk

window = tk.Tk()
window.title("Using Observable Variables")
window.geometry("700x500")

# Observable variables
name_var =tk.StringVar()
age_var = tk.IntVar()
message_var = tk.StringVar()

#functiom to update message
def update_message(*args):
    name = name_var.get()
    age = age_var.get()
    if name and age:
        try:
            age_int = int(age)
            message_var.set(f"Hello, {name}! You are {age_int} years old.")
        except ValueError:
            message_var.set("Please enter a valid age.")
    else:
        message_var.set("Please enter your name and age.")

#add observers
name_var.trace_add("write", update_message)    
age_var.trace_add("write", update_message) 

#labels and user inputs
tk.Label(window, text="Name:").grid(row=0, column=0)
tk.Entry(window, textvariable=name_var).grid(row=0, column=1)


tk.Label(window, text="Age:").grid(row=1, column=0)
tk.Entry(window, textvariable=age_var).grid(row=1, column=1)

#lebel message
tk.Label(window, textvariable=message_var).grid(row=2, column=0, columnspan=2)


#run 
window.mainloop()
