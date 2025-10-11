import tkinter as tk

#create the main window
root = tk.Tk()
root.title("Form Using Grid Method")

#create label widgets
name_label = tk.Label(root, text="Name:")
email_label = tk.Label(root,text="Email:")
password_label = tk.Label(root, text="Password:")

#cretae entry widgets(text boxes)
name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*") #show="*" to hide the password


#use grid method to arrange everything
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e") #stick to east (right)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry.grid(row=1, column=1, padx=10, pady=5)

password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_entry.grid(row=2, column=1, padx=10, pady=5)

#run
root.mainloop()