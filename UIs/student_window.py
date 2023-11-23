import tkinter as tk
import customtkinter as c
from center_window import center_window

# def create_search_window(tab):
#     tab.destroy()
#
#     tab = c.CTkFrame(window)
#     tab.grid(row=0, column=1, columnspan=5, rowspan=4, sticky="news", padx=10, pady=10)
#
#     search_bar = c.CTkEntry(tab, width=650, placeholder_text=" S E A R C H ")
#     search_bar.grid(row=0, column=0, columnspan=3, sticky="news", padx=10, pady=10)
#
#     refresh = c.CTkButton(tab, text="@", command=lambda: fill_treeview(tree))
#     refresh.grid(row=0, column=3)
#
#     tree = ttk.Treeview(tab, columns=('Roll Number', 'Name', 'Class', 'Date of Birth', 'Gender', 'Phone Number', 'Guardian Name', 'Address'))
#
#     tree.heading('Roll Number', text='Roll Number')
#     tree.heading('Name', text='Name')
#     tree.heading('Class', text='Class')
#     tree.heading('Date of Birth', text='Date of Birth')
#     tree.heading('Gender', text='Gender')
#     tree.heading('Phone Number', text='Phone Number')
#     tree.heading('Guardian Name', text='Guardian Name')
#     tree.heading('Address', text='Address')
#
#     # Populate the Treeview with data
#     fill_treeview(tree)
#
#     # Add Treeview to the GUI
#     tree.grid(row=1, column=0, columnspan=4, sticky="news")
#     tree.grid(row=1, column=0, columnspan=4, sticky="news")
#
#     # Configure row and column weights
#     tab.grid_rowconfigure(1, weight=1)
#     tab.grid_columnconfigure(0, weight=1)
#     tab.grid_columnconfigure(1, weight=1)
#     tab.grid_columnconfigure(2, weight=1)
#     tab.grid_columnconfigure(3, weight=1)



def create_student_window(rollno):

    root = c.CTk()
    root.title("Student Form")
    root.columnconfigure(1, weight=3, uniform="a")
    root.columnconfigure(2, weight=7, uniform="a")

    frame_panel = c.CTkFrame(root)
    frame_panel.grid(row=0, column=0, sticky="news", padx=10, pady=10)

    frame_view = c.CTkFrame(root)
    frame_view.grid(row=0, column=1, sticky="news", padx=10, pady=10)


    # Create labels and entry fields
    roll_number_label = c.CTkLabel(frame_panel, text="Roll Number")
    roll_number_label.grid(row=0, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    roll_number_entry = c.CTkEntry(frame_panel)
    roll_number_entry.grid(row=0, column=1, sticky="we", padx=(0, 10), pady=(10, 0))

    name_label = c.CTkLabel(frame_panel, text="Name")
    name_label.grid(row=1, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    name_entry = c.CTkEntry(frame_panel)
    name_entry.grid(row=1, column=1, sticky="we", padx=(0, 10), pady=(10, 0))

    class_label = c.CTkLabel(frame_panel, text="Class")
    class_label.grid(row=2, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    class_entry = c.CTkEntry(frame_panel)
    class_entry.grid(row=2, column=1, sticky="we", padx=(0, 10), pady=(10, 0))

    dob_label = c.CTkLabel(frame_panel, text="Date Of Birth")
    dob_label.grid(row=3, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    dob_entry = c.CTkEntry(frame_panel)
    dob_entry.grid(row=3, column=1, sticky="we", padx=(0, 10), pady=(10, 0))

    gender_label = c.CTkLabel(frame_panel, text="Gender")
    gender_label.grid(row=4, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    gender_entry = c.CTkEntry(frame_panel)
    gender_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=(0, 10), pady=(10, 0))

    phone_label = c.CTkLabel(frame_panel, text="Phone Number")
    phone_label.grid(row=5, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    phone_entry = c.CTkEntry(frame_panel)
    phone_entry.grid(row=5, column=1, sticky="we", padx=(0, 10), pady=(10, 0))

    guardian_label = c.CTkLabel(frame_panel, text="Guardians Name")
    guardian_label.grid(row=6, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    guardian_entry = c.CTkEntry(frame_panel)
    guardian_entry.grid(row=6, column=1, sticky="we", padx=(0, 10), pady=(10, 0))

    address_label = c.CTkLabel(frame_panel, text="Address")
    address_label.grid(row=7, column=0, sticky="w", padx=(10, 0), pady=(10, 0))
    address_entry = c.CTkEntry(frame_panel)
    address_entry.grid(row=7, column=1, sticky="we", padx=(0, 10), pady=(10, 0))

    submit_button = c.CTkButton(frame_panel, text="Submit")
    submit_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()

create_student_window(3)

