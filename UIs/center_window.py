import tkinter as tk

def center_window(window):
    # Get the screen resolution
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Get the window size
    window.update_idletasks()  # Ensure that the window size is updated
    req_width = window.winfo_reqwidth()
    req_height = window.winfo_reqheight()

    # Calculate the X and Y coordinates to center the window
    x = (screen_width - req_width) // 2
    y = (screen_height - req_height*1.5) // 2

    # Set the position of the window
    window.geometry(f"+{x}+{y}")

