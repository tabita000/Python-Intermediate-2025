import tkinter as tk

# creating the main window
window = tk.Tk()
window.title("Data Entry Form")

# creating static label text
static_label = tk.Label(window, text="Please enter your information below:")
static_label.pack()

# creating a dynamic text label using a text variable
dynamic_text = tk.StringVar()
dynamic_text.set("This is a dynamic text label.")
dynamic_label = tk.Label(window, textvariable=dynamic_text, fg="blue")
dynamic_label.pack()

# create a message widget
message = tk.Message(window, text="Widget to display data")
message.pack()

# create a frame to hold widgets
frame = tk.Frame(window, bd=2, relief=tk.SUNKEN)
frame.pack(padx=10, pady=10)

# add a label to the label frame
label_in_frame = tk.Label(frame, text="Label inside a Frame")
label_in_frame.pack

# create an entry, a widget for user input
entry = tk.Entry(window)
entry.pack()

# create a button to fetch the entry data and display it in a label
def show_entry_data():
    entered_text = entry.get()
    dynamic_text.set(entered_text)
    
button = tk.Button(window, text="Show Entry Data", command=show_entry_data)
button.pack()    

# run
window.mainloop()