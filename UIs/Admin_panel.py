import customtkinter as c
from CTkTable import CTkTable
from backend import *


def create_student_window():
    root = c.CTk()
    root.title("Student Form")
    root.resizable(False, False)
    root.columnconfigure(1, weight=3, uniform="a")
    root.columnconfigure(2, weight=7, uniform="a")

    def panel_selector(value, frame):
        frame.destroy()

        frame = c.CTkFrame(root)
        frame.grid(row=1, column=0, sticky="news", padx=10, pady=10)

        if value == "Delete":
            # Roll Number Label and Entry
            roll_number_label = c.CTkLabel(frame, text="Roll Number to be deleted ")
            roll_number_label.grid(row=0, column=0, sticky="we", columnspan=3, padx=10, pady=(10, 0))

            roll_number_entry = c.CTkEntry(frame)
            roll_number_entry.grid(row=1, column=0, sticky="we", columnspan=3, padx=10, pady=(0, 10))

            # Instruction Label
            instruct = c.CTkLabel(frame,
                                  text="All the data of the student with the selected roll number will be deleted")
            instruct.grid(row=0, column=3, columnspan=3, sticky="news", padx=10, pady=(10, 0))

            # Delete Button
            delete_button_button = c.CTkButton(frame, text="Delete",
                                               command=lambda: delete_student_record(roll_number_entry.get()))
            delete_button_button.grid(row=3, column=0, columnspan=3, sticky="we", padx=10, pady=10)


        elif value == "Update":
            # Roll Number Label and Entry
            roll_number_label = c.CTkLabel(frame, text="Roll Number")
            roll_number_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

            roll_number_entry = c.CTkEntry(frame)
            roll_number_entry.grid(row=1, column=0, sticky="we", padx=10, pady=(0, 10))

            # Field to Update Label and Combobox
            field_label = c.CTkLabel(frame, text="Field to Update")
            field_label.grid(row=0, column=1, sticky="w", padx=10, pady=(10, 0))

            fields = ["Name", "Class", "Date_Of_Birth", "Gender", "Phone_Number", "Guardians_Name", "Address"]
            field_combobox = c.CTkOptionMenu(frame, values=fields)
            field_combobox.grid(row=1, column=1, sticky="we", padx=10, pady=(0, 10))

            # New Value Label and Entry
            new_value_label = c.CTkLabel(frame, text="New Value")
            new_value_label.grid(row=0, column=2, sticky="w", padx=10, pady=(10, 0))

            new_value_entry = c.CTkEntry(frame)
            new_value_entry.grid(row=1, column=2, sticky="we", padx=10, pady=(0, 10))

            # Update Button
            update_data_button = c.CTkButton(frame, text="Update",
                                             command=lambda: update_student_record(roll_number_entry.get(),
                                                                                   field_combobox.get(),
                                                                                   new_value_entry.get())
                                             )
            update_data_button.grid(row=2, column=0, columnspan=2, sticky="we", padx=10, pady=10)

        else:
            # Create labels and entry fields
            roll_number_label = c.CTkLabel(frame, text="Roll Number")
            roll_number_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))
            roll_number_entry = c.CTkEntry(frame)
            roll_number_entry.grid(row=1, column=0, sticky="we", padx=10, pady=(0, 10))

            name_label = c.CTkLabel(frame, text="Name")
            name_label.grid(row=0, column=1, sticky="w", padx=10, pady=(10, 0))
            name_entry = c.CTkEntry(frame)
            name_entry.grid(row=1, column=1, sticky="we", padx=10, pady=(0, 10))

            class_label = c.CTkLabel(frame, text="Class")
            class_label.grid(row=0, column=2, sticky="w", padx=10, pady=(10, 0))
            class_entry = c.CTkEntry(frame)
            class_entry.grid(row=1, column=2, sticky="we", padx=10, pady=(0, 10))

            dob_label = c.CTkLabel(frame, text="Date Of Birth")
            dob_label.grid(row=0, column=3, sticky="w", padx=10, pady=(10, 0))
            dob_entry = c.CTkEntry(frame)
            dob_entry.grid(row=1, column=3, sticky="we", padx=10, pady=(0, 10))

            gender_label = c.CTkLabel(frame, text="Gender")
            gender_label.grid(row=0, column=4, sticky="w", padx=10, pady=(10, 0))
            gender_entry = c.CTkEntry(frame)
            gender_entry.grid(row=1, column=4, sticky="we", padx=10, pady=(0, 10))

            phone_label = c.CTkLabel(frame, text="Phone Number")
            phone_label.grid(row=0, column=5, sticky="w", padx=10, pady=(10, 0))
            phone_entry = c.CTkEntry(frame)
            phone_entry.grid(row=1, column=5, sticky="we", padx=10, pady=(0, 10))

            guardian_label = c.CTkLabel(frame, text="Guardians Name")
            guardian_label.grid(row=0, column=6, sticky="w", padx=10, pady=(10, 0))
            guardian_entry = c.CTkEntry(frame)
            guardian_entry.grid(row=1, column=6, sticky="we", padx=10, pady=(0, 10))

            address_label = c.CTkLabel(frame, text="Address")
            address_label.grid(row=0, column=7, sticky="w", padx=10, pady=(10, 0))
            address_entry = c.CTkEntry(frame)
            address_entry.grid(row=1, column=7, sticky="we", padx=10, pady=(0, 10))

            insert_data_button = c.CTkButton(frame, text="insert", command=lambda: insert_student_record(
                roll_number_entry.get(), name_entry.get(), class_entry.get(), dob_entry.get(), gender_entry.get(),
                phone_entry.get(), guardian_entry.get(), address_entry.get()))

            insert_data_button.grid(row=2, column=0, columnspan=2, sticky="we", padx=10, pady=10)

    frame_panel = c.CTkFrame(root)
    frame_panel.grid(row=1, column=0, sticky="news", padx=10, pady=(0, 10))

    seg_selector = c.CTkSegmentedButton(root, values=["Insert", "Update", "Delete"],
                                        command=lambda value, frame=frame_panel: panel_selector(value, frame))
    seg_selector.grid(row=0, column=0, sticky="news", padx=10, pady=(10, 0))
    seg_selector.set("Insert")

    panel_selector("Insert", frame_panel)

    frame_headings = c.CTkFrame(root)
    frame_headings.grid(row=2, column=0, sticky="news", padx=10, pady=(10, 0))

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

        if new_data != previous_data:  # i.e. there is a change in data
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
    scrollable_frame.grid(row=3, column=0, sticky="news", padx=10, pady=(5, 10))

    initial_data = get_all_data()

    table_widget = CTkTable(scrollable_frame, row=20, column=8, values=initial_data)
    table_widget.grid(sticky="nsew", columnspan=8)

    update_table(initial_data, table_widget)

    root.mainloop()
