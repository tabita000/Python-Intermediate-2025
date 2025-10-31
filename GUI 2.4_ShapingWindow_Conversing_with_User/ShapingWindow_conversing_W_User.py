import tkinter as tk
from tkinter import messagebox

# creating the main window & window size
window = tk.Tk()
window.geometry("400x200")

#set minimum and max size of window
window.minsize(300,200)
window.maxsize(600,400)

#title of the window
window.title("Shaping Window: Conversing with User")

#window icon
window.iconbitmap("icon-multi.ico")

#define function to handle window
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
#bind the function to window close event
window.protocol("WM_DELETE_WINDOW", on_closing)

#Message box functions
def show_error():
    messagebox.showerror("Error", "An error has occurred!")
    
def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")
    
def show_info():
    messagebox.showinfo("Information", "This is an informational message.")
    
#conversation function
def ask_yes_no():
    response = messagebox.askyesno("Question ", "Would you like to proceed?")
    if response:
        print("User chose Yes")
    else:
        print("User chose No")
        
def ask_ok_cancel():
    response = messagebox.askokcancel("Confirmation", "Do you want to continue?")
    if response:
        print("User chose OK")
    else:
        print("User chose Cancel")  
        
def ask_retry_cancel():
    response = messagebox.askretrycancel("Retry", "Operation failed. Would you like to retry?")
    if response:
        print("User chose Retry")
    else:
        print("User chose Cancel")    
        
#Buttons to trigger each example
tk.Button(window, text="Show Error", command=show_error).pack(pady=5)
tk.Button(window, text="Show Warning", command=show_warning).pack(pady=5)
tk.Button(window, text="Show Info", command=show_info).pack(pady=5)
tk.Button(window, text="Ask Yes/No", command=ask_yes_no).pack(pady=5)
tk.Button(window, text="Ask OK/Cancel", command=ask_ok_cancel).pack(pady=5)
tk.Button(window, text="Ask Retry/Cancel", command=ask_retry_cancel).pack(pady=5)                  

#run
window.mainloop()