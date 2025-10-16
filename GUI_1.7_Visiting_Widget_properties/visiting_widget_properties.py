# customizing TKinter widgets
import tkinter as tk

#main window
window = tk.Tk()
window.title("Customizing Widgets")
window.geometry("400x300")
window.configure(bg="white")

#btn color and cursor
btn1 = tk.Button(window, text="Red Button", fg="black", bg="red", cursor="hand2")
btn1.pack(pady=10)

btn2 = tk.Button(window, text="Green Button", fg="black", bg="lightgreen", cursor="circle")
btn2.pack(pady=10)

btn3 = tk.Button(window, text="Blue Button", fg="purple", bg="blue", cursor="cross")
btn3.pack(pady=10)

#labels (fonts + anchors)
label1 = tk.Label(window, text="This is text for label 1", font=("Arial", 12), anchor="w") #west or left
label1.pack(pady=6, fill='x')

label2 = tk.Label(window, text="This is text for label 2", font=("Times New Roman", 14, "bold"), anchor="e") #east or right
label2.pack(pady=6 ,fill='x')

label3 = tk.Label(window, text="This is text for label 3", font=("Helvetica", 10, "italic"), anchor="n") #north or top
label3.pack(pady=6, fill='x')

#run
window.mainloop()

#NOTES
# 3 buttons use different colors and cursors.

# 3 labels use different fonts/sizes/styles and anchors (w, e, n).

# Widgets arranged with pack(); window created with Tk() and titled.