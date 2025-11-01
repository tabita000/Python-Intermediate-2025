import tkinter as tk
from tkinter import messagebox

#window, title and size
window = tk.Tk()
window.title("Simple Pocket Calculator")
window.geometry("300x400")

#display box
display = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
display.grid(row=0, column=0, columnspan=4)

#functions
#insert
def add_char(ch):
    display.insert(tk.END, ch)
    
#delete
def delete_display():
    display.delete(0, tk.END)
    
#calculate
def calculate():
   calculation = display.get().replace('×', '*').replace('÷', '/')
   try:
       result = eval(calculation)
       display.delete(0, tk.END)
       display.insert(tk.END, str(result))
   except Exception:
       messagebox.showerror("Error", "Invalid Input")
       delete_display()
       
#number buttons
def press_1(): add_char('1')
def press_2(): add_char('2')
def press_3(): add_char('3')
def press_4(): add_char('4')
def press_5(): add_char('5')
def press_6(): add_char('6')
def press_7(): add_char('7')
def press_8(): add_char('8')
def press_9(): add_char('9')
def press_0(): add_char('0')
def press_dot(): add_char('.')
def press_plus(): add_char('+')
def press_minus(): add_char('-')
def press_multiply(): add_char('×')
def press_divide(): add_char('÷')

#buttons       
tk.Button(window, text="7", width=5, height=2, font=("Arial", 16), command=press_7).grid(row=1, column=0)
tk.Button(window, text="8", width=5, height=2, font=("Arial", 16), command=press_8).grid(row=1, column=1)
tk.Button(window, text="9", width=5, height=2, font=("Arial", 16), command=press_9).grid(row=1, column=2)
tk.Button(window, text="÷", width=5, height=2, font=("Arial", 16), command=press_divide).grid(row=1, column=3)

tk.Button(window, text="4", width=5, height=2, font=("Arial", 16), command=press_4).grid(row=2, column=0)
tk.Button(window, text="5", width=5, height=2, font=("Arial", 16), command=press_5).grid(row=2, column=1)
tk.Button(window, text="6", width=5, height=2, font=("Arial", 16), command=press_6).grid(row=2, column=2)
tk.Button(window, text="×", width=5, height=2, font=("Arial", 16), command=press_multiply).grid(row=2, column=3)

tk.Button(window, text="1", width=5, height=2, font=("Arial", 16), command=press_1).grid(row=3, column=0)
tk.Button(window, text="2", width=5, height=2, font=("Arial", 16), command=press_2).grid(row=3, column=1)
tk.Button(window, text="3", width=5, height=2, font=("Arial", 16), command=press_3).grid(row=3, column=2)
tk.Button(window, text="-", width=5, height=2, font=("Arial", 16), command=press_minus).grid(row=3, column=3)

tk.Button(window, text="C", width=5, height=2, font=("Arial", 16), command=delete_display).grid(row=4, column=0)
tk.Button(window, text="0", width=5, height=2, font=("Arial", 16), command=press_0).grid(row=4, column=1)
tk.Button(window, text=".", width=5, height=2, font=("Arial", 16), command=press_dot).grid(row=4, column=2)
tk.Button(window, text="+", width=5, height=2, font=("Arial", 16), command=press_plus).grid(row=4, column=3)

tk.Button(window, text="=", width=23, height=2, font=("Arial", 16), command=calculate).grid(row=5, column=0, columnspan=4)

#run
window.mainloop()