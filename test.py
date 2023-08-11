import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def perform_search():
    query = search_entry.get()
    search_results_label.config(text=f"Searching for: {query}")

# Create the main window
root = tk.Tk()
root.title("Search Bar Example")

# Apply the themed style to the entire application
style = ThemedStyle(root)
style.set_theme("arc")  # You can choose a theme from available options

# Create and place the search entry widget
search_entry = ttk.Entry(root, width=40)
search_entry.pack(padx=10, pady=10)

# Create and place the search button
search_button = ttk.Button(root, text="Search", command=perform_search)
search_button.pack()

# Create and place a label to display search results or status
search_results_label = ttk.Label(root, text="", font=("Helvetica", 12))
search_results_label.pack(pady=10)

root.mainloop()




