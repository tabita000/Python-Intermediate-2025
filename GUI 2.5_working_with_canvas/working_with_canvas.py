import tkinter as tk

#create the main window and title
window = tk.Tk()
window.title("Christmas Tree Canvas")

# create a canvas (width, heigt, bg color)
canvas = tk.Canvas(window, width=400, height=400, bg="lightblue", borderwidth=2)
canvas.pack()

#draw tree - three green triangles
canvas.create_polygon(200, 60, 260, 160, 140, 160, outline="green", fill="green", width=2)
canvas.create_polygon(200, 120, 280, 240, 120, 240, outline="green", fill="green", width=2)
canvas.create_polygon(200, 200, 300, 320, 100, 320, outline="green", fill="green", width=2)

#draw trunk - brown rectangle
canvas.create_rectangle(175, 300, 225, 350, outline="brown", fill="brown", width=2)

#draw star - yellow polygon
# star (5-point)
canvas.create_polygon(
200,40, 206,58, 226,58, 210,70, 216,88,
200,78, 184,88, 190,70, 174,58, 194,58,
outline="gold", fill="gold", width=2)

#ornaments
canvas.create_oval(180, 120, 190, 130, outline="red", fill="red", width=2)

canvas.create_oval(210, 120, 220, 130, outline="yellow", fill="yellow", width=2)

canvas.create_oval(195, 100, 205, 110, outline="blue", fill="blue", width=2)

#message
canvas.create_text(200, 370, text="Merry Christmas!", font=("Arial", 16), fill="darkred")

#run
window.mainloop()

