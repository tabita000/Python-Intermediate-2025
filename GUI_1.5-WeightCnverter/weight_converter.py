import tkinter as tk

#main window
root = tk.Tk()
root.title("Weight Converter")
root.geometry("300x200")

#frame
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

#amount input
label = tk.Label(frame, text="Enter weight in pounds:")
label.pack()
weight_entry = tk.Entry(frame)
weight_entry.pack()

#conversion type - radio buttons
conversion_type = tk.StringVar(value="lb_to_kg")

radio_btn1 = tk.Radiobutton(frame, text="Pounds to Kilograms", variable=conversion_type, value="lb_to_kg")
radio_btn1.pack(anchor='w')

radio_btn2 = tk.Radiobutton(frame, text="Kilograms to Pounds", variable=conversion_type, value="kg_to_lb")
radio_btn2.pack(anchor='w')

#result display - will start empty
result_label = tk.Label(frame, text="")
result_label.pack(pady=(6,0))

#conversion function +logic
def calculate():
    try:
        amount = float(weight_entry.get())
        if conversion_type.get() == "lb_to_kg":
            converted = amount * 0.453592
            result_label.config(text=f"{amount} lbs = {converted:.2f} kg")
        else: #kg_to_lb
            converted = amount / 0.453592
            result_label.config(text=f"{amount} kg = {converted:.2f} lbs")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        
tk.Button(frame, text="Calculate", command=calculate).pack(pady=(6,0))        

#run
root.mainloop()