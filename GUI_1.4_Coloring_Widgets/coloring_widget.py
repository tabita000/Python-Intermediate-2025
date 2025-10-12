import tkinter as tk

root = tk.Tk()
root.title("Coloring Widgets")

# helper: make a solid-color image
def solid_img(color, w=160, h=32):
    img = tk.PhotoImage(width=w, height=h)
    img.put(color, to=(0, 0, w, h))
    return img

# shared normal (gray) image
NORMAL_IMG = solid_img("#E0E0E0")   # neutral gray like a system button

# handlers function
def on_press(event):
    event.widget.config(image=event.widget.pressed_img)
def on_release(event):
    event.widget.config(image=event.widget.normal_img)

#Button 1
tk.Label(root, text="Button 1").grid(row=0, column=0, padx=10, pady=6, sticky="e")
b1 = tk.Button(root, text="Click Me", fg="black", image=NORMAL_IMG, compound="center", bd=1, relief="raised")
b1.normal_img = NORMAL_IMG
b1.pressed_img = solid_img("#4BE04B")
b1.grid(row=0, column=1, padx=10, pady=6, sticky="w")
b1.bind("<ButtonPress-1>", on_press)
b1.bind("<ButtonRelease-1>", on_release)

#Button 2
tk.Label(root, text="Button 2").grid(row=1, column=0, padx=10, pady=6, sticky="e")
b2 = tk.Button(root, text="No, Click Me", fg="black", image=NORMAL_IMG, compound="center", bd=1, relief="raised")
b2.normal_img = NORMAL_IMG
b2.pressed_img = solid_img("#EEC066")
b2.grid(row=1, column=1, padx=10, pady=6, sticky="w")
b2.bind("<ButtonPress-1>", on_press)
b2.bind("<ButtonRelease-1>", on_release)

#Button 3
tk.Label(root, text="Button 3").grid(row=2, column=0, padx=10, pady=6, sticky="e")
b3 = tk.Button(root, text="Don't Click Me", fg="black", image=NORMAL_IMG, compound="center", bd=1, relief="raised")
b3.normal_img = NORMAL_IMG
b3.pressed_img = solid_img("#64B6D2")
b3.grid(row=2, column=1, padx=10, pady=6, sticky="w")
b3.bind("<ButtonPress-1>", on_press)
b3.bind("<ButtonRelease-1>", on_release)


#run
root.mainloop()
