import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Multi-button GUI")
window.geometry("300x200")
window.configure(bg="lightblue")

def change_color():
    current_color = window.cget("bg")
    if current_color == "lightblue":
        window.configure(bg="lightgreen")
    else:
        window.configure(bg="lightblue")
        
# function to show lines one at a time
some_lines = [
    "Itsy bitsy spider climbed up the waterspout",
    "Down came the rain and washed the spider out",
    "Out came the sun and dried up all the rain",
    "And the itsy bitsy spider climbed up the spout again"
]       
line_index = 0
def show_next_line():
    global line_index
    if line_index < len(some_lines):
        messagebox.showinfo("Line", some_lines[line_index])
        line_index += 1
    else:
        messagebox.showinfo("End", "No more lines to show.")
        line_index = 0  # Reset for next time
        

# Function for extra action: show number of clicks
click_count = 0
def count_clicks():
    global click_count
    click_count += 1
    messagebox.showinfo("Click Count", f"Button clicked {click_count} times.")
    
# create buttons and pack
color_button = tk.Button(window, text="Change Color", command=change_color)
color_button.pack(pady=10)

line_button = tk.Button(window, text="Show Next Line", command=show_next_line)
line_button.pack(pady=10)

count_button = tk.Button(window, text="Count Clicks", command=count_clicks)
count_button.pack(pady=10)          

#run
window.mainloop()