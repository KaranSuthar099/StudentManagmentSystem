import tkinter as tk
import customtkinter as c
from CTkTable import CTkTable

from backend import get_all_data
from center_window import center_window


def create_student_window(rollno):
    root = c.CTk()
    root.title("Student Form")
    root.columnconfigure(1, weight=3, uniform="a")
    root.columnconfigure(2, weight=7, uniform="a")

    frame_panel = c.CTkFrame(root)
    frame_panel.grid(row=0, column=0, sticky="news", padx=10, pady=10)

    # Create labels and entry fields
    roll_number_label = c.CTkLabel(frame_panel, text="Roll Number")
    roll_number_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    roll_number_entry = c.CTkEntry(frame_panel)
    roll_number_entry.grid(row=1, column=0, sticky="we", padx=10, pady=10)

    name_label = c.CTkLabel(frame_panel, text="Name")
    name_label.grid(row=0, column=1, sticky="w", padx=10, pady=10)
    name_entry = c.CTkEntry(frame_panel)
    name_entry.grid(row=1, column=1, sticky="we", padx=10, pady=10)

    class_label = c.CTkLabel(frame_panel, text="Class")
    class_label.grid(row=0, column=2, sticky="w", padx=10, pady=10)
    class_entry = c.CTkEntry(frame_panel)
    class_entry.grid(row=1, column=2, sticky="we", padx=10, pady=10)

    dob_label = c.CTkLabel(frame_panel, text="Date Of Birth")
    dob_label.grid(row=0, column=3, sticky="w", padx=10, pady=10)
    dob_entry = c.CTkEntry(frame_panel)
    dob_entry.grid(row=1, column=3, sticky="we", padx=10, pady=10)

    gender_label = c.CTkLabel(frame_panel, text="Gender")
    gender_label.grid(row=0, column=4, sticky="w", padx=10, pady=10)
    gender_entry = c.CTkEntry(frame_panel)
    gender_entry.grid(row=1, column=4, sticky="we", padx=10, pady=10)

    phone_label = c.CTkLabel(frame_panel, text="Phone Number")
    phone_label.grid(row=0, column=5, sticky="w", padx=10, pady=10)
    phone_entry = c.CTkEntry(frame_panel)
    phone_entry.grid(row=1, column=5, sticky="we", padx=10, pady=10)

    guardian_label = c.CTkLabel(frame_panel, text="Guardians Name")
    guardian_label.grid(row=0, column=6, sticky="w", padx=10, pady=10)
    guardian_entry = c.CTkEntry(frame_panel)
    guardian_entry.grid(row=1, column=6, sticky="we", padx=10, pady=10)

    address_label = c.CTkLabel(frame_panel, text="Address")
    address_label.grid(row=0, column=7, sticky="w", padx=10, pady=10)
    address_entry = c.CTkEntry(frame_panel)
    address_entry.grid(row=1, column=7, sticky="we", padx=10, pady=10)

    insert_data = c.CTkButton(frame_panel, text="Submit")
    insert_data.grid(row=2, column=0, columnspan=2, sticky="we", padx=10, pady=10)

    update_data = c.CTkButton(frame_panel, text="Submit")
    update_data.grid(row=2, column=2, columnspan=2, sticky="we", padx=10, pady=10)

    delete_data = c.CTkButton(frame_panel, text="Submit")
    delete_data.grid(row=2, column=4, columnspan=2, sticky="we", padx=10, pady=10)



    frame_headings = c.CTkFrame(root)
    frame_headings.grid(row=1, column=0, sticky="news", padx=10, pady=(10, 0))

    labels = \
        [c.CTkLabel(frame_headings, text="Roll Number", width=150),
         c.CTkLabel(frame_headings, text="Name", width=150),
         c.CTkLabel(frame_headings, text="Class", width=130),
         c.CTkLabel(frame_headings, text="Date Of Birth", width=150),
         c.CTkLabel(frame_headings, text="Gender", width=140),
         c.CTkLabel(frame_headings, text="Phone Number", width=130),
         c.CTkLabel(frame_headings, text="Guardians Name", width=200),
         c.CTkLabel(frame_headings, text="Address", width=150)]
    # Applying characteristics to each label
    for label in labels:
        label.grid(row=0, column=labels.index(label), sticky="we")



    def update_table(previous_data, table):
        new_data = get_all_data()
        new_data = [(tup[:-1] if isinstance(tup[-1], str) else tup) for tup in new_data]

        if new_data != previous_data:  # i.e there is a change in data
            table.destroy()
            previous_data = new_data
            if len(new_data) > 12:
                table = CTkTable(scrollable_frame, row=len(new_data), column=8, values=previous_data)
                table.grid(sticky="nsew", columnspan=8)
            else:
                table = CTkTable(scrollable_frame, row=12, column=8, values=previous_data)
                table.grid(sticky="nsew", columnspan=8)  # to not change the number of rows

        root.after(5000, update_table, previous_data, table)  # pass the reference, not the result of the function call

    scrollable_frame = c.CTkScrollableFrame(root, width=1200, height=400)
    scrollable_frame.grid(row=2, column=0, sticky="news", padx=10, pady=(5, 10))

    initial_data = get_all_data()
    initial_data = [(tup[:-1] if isinstance(tup[-1], str) else tup) for tup in initial_data]

    table_widget = CTkTable(scrollable_frame, row=50, column=8, values=initial_data)
    table_widget.grid(sticky="nsew", columnspan=8)

    update_table(initial_data, table_widget)

    root.mainloop()

create_student_window(3)
