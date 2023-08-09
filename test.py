import tkinter as tk

def on_entry_click(event):
    if entry.get() == "Enter your text here":
        entry.delete(0, "end")  # Clear the placeholder text when clicked
        entry.config(fg="black")  # Change text color to black


def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Enter your text here")
        entry.config(fg="gray")  # Change text color back to gray

root = tk.Tk()
root.geometry("300x100")

entry = tk.Entry(root, fg="gray")
entry.insert(0, "Enter your text here")
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)
entry.pack()

root.mainloop()
