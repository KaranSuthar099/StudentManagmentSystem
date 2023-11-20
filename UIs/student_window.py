import tkinter as tk
import customtkinter as c
from center_window import center_window

def create_student_window():
    import tkinter as tk
    from tkinter import ttk

    def submit_form():
        # You can handle form submission here
        pass

    root = tk.Tk()
    root.title("Student Form")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Create labels and entry fields
    roll_number_label = ttk.Label(frame, text="Roll Number")
    roll_number_label.grid(row=0, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    roll_number_entry = ttk.Entry(frame)
    roll_number_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    name_label = ttk.Label(frame, text="Name")
    name_label.grid(row=1, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    name_entry = ttk.Entry(frame)
    name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    class_label = ttk.Label(frame, text="Class")
    class_label.grid(row=2, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    class_entry = ttk.Entry(frame)
    class_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    dob_label = ttk.Label(frame, text="Date Of Birth")
    dob_label.grid(row=3, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    dob_entry = ttk.Entry(frame)
    dob_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    gender_label = ttk.Label(frame, text="Gender")
    gender_label.grid(row=4, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    gender_entry = ttk.Entry(frame)
    gender_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    phone_label = ttk.Label(frame, text="Phone Number")
    phone_label.grid(row=5, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    phone_entry = ttk.Entry(frame)
    phone_entry.grid(row=5, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    guardian_label = ttk.Label(frame, text="Guardians Name")
    guardian_label.grid(row=6, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    guardian_entry = ttk.Entry(frame)
    guardian_entry.grid(row=6, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    address_label = ttk.Label(frame, text="Address")
    address_label.grid(row=7, column=0, sticky=tk.W, padx=(10, 0), pady=(10, 0))
    address_entry = ttk.Entry(frame)
    address_entry.grid(row=7, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    submit_button = ttk.Button(frame, text="Submit", command=submit_form)
    submit_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()
