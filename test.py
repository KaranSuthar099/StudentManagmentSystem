import tkinter as tk

def create_window1(root):
    root.destroy()
    window1 = tk.Tk()
    button = tk.Button(window1, text="Go to Window 2", command=lambda: create_window2(window1))
    button.pack()
    window1.mainloop()

def create_window2(root):
    root.destroy()
    window2 = tk.Tk()
    button = tk.Button(window2, text="Go to Window 1", command=lambda: create_window1(window2))
    button.pack()
    window2.mainloop()

root = tk.Tk()
button = tk.Button(root, text="Go to Window 1", command=lambda: create_window1(root))
button.pack()
root.mainloop()