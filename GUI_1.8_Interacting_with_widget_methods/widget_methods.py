#Event Programming with Widgets

import tkinter as tk

# main window
window = tk.Tk()
window.title("Widget Methods Example")
window.geometry("400x300")
window.configure(bg="lightgray")

#change back coloe after two seconds
def change_color():
    window.configure(bg="pink")
window.after(2000, change_color) #3000 milliseconds (3 seconds)


#close window with goodbye btn
goodbye_btn = tk.Button(window, text="Click Goodbye Btn", command=window.destroy)
goodbye_btn.pack(pady=20)
goodbye_btn.focus_set() # spacebar destroys window.


# change window size button.
def change_size():
    window.geometry("800x400")
size_btn = tk.Button(window, text="Change Size", command=change_size)
size_btn.pack(pady=20)

# change text of goodbye button.
def change_text():
    goodbye_btn.config(text="Goodbye!")
    
text_btn = tk.Button(window, text="Change Goodbye Btn Text", command=change_text)
text_btn.pack(pady=20)    

#run
window.mainloop()