import tkinter as tk
from tkinter import messagebox

#window box
window = tk.Tk()
window.title("Joke")
window.geometry("400x300")

#label
label = tk.Label(window, text="why did the computer get cold?", font="Cursive 20 bold", fg="blue") #fg is txt clr , bg is background clr
label.pack(pady=20) # pady is padding in y axis

#button click
def on_button_click():
    label.config(text="because it left its Windows open!") 
    
answer_button = tk.Button(window, text="Click for answer", command=on_button_click, bg="lightgreen", fg="black", font="Arial 14")
answer_button.pack(pady=10)  


#exit button
def exit_app():
    window.quit() 

exit_button = tk.Button(window, text="Exit", command=exit_app, bg="red", fg="black", font="Arial 14")
exit_button.pack(pady=10)  

window.mainloop()
      