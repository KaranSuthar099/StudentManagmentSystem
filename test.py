import tkinter as tk

def move_rectangle():
    canvas.move(rectangle, 1, 0)
    root.after(10, move_rectangle)  # Schedule the next move after 10 milliseconds

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

rectangle = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

move_rectangle()

root.mainloop()

