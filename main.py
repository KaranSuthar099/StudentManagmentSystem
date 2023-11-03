import tkinter as tk

import customtkinter as c

from backend import *

c.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# def remove_focus_sidebar(_):
#     # Remove focus from the widget that currently has focus
#     sidebar.focus()
#
# def remove_focus_mainframe(_):
#     mainframe.focus_set()
#
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
#
# def create_delete_window(tab):
#     tab.destroy()
#
#     tab = c.CTkFrame(window)
#     tab.grid(row=0, column=1, columnspan=5, rowspan=4, sticky="news", padx=10, pady=10)
#
#     delete_roll_label = c.CTkLabel(tab, text="Roll Number ")
#     delete_roll_label.grid(row=0, column=0, sticky="news", padx=5, pady=5)
#
#     delete_entry_roll = c.CTkEntry(tab, width=300, placeholder_text="of whose data is to be Deleted")
#     delete_entry_roll.grid(row=0, column=1, columnspan=2, sticky="news", padx=5, pady=5)
#
#     enter_button_delete = c.CTkButton(tab, text="Enter",
#                                       command=lambda: delete_student_record(delete_entry_roll.get())
#                                       )
#     enter_button_delete.grid(row=1, column=1, columnspan=2, padx=10, pady=30, sticky="news")
#
#
# def create_update_window(tabs):
#     tabs.destroy()
#
#     tabs = c.CTkFrame(window)
#     tabs.grid(row=0, column=1, columnspan=5, rowspan=4, sticky="news", padx=10, pady=10)
#     # update student tab
#
#     update_label = c.CTkLabel(tabs, text="You want to Update ")
#     update_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#
#     update_options = c.CTkOptionMenu(
#         tabs,
#         command=lambda: select_update_value(tab=tabs),
#         values=[
#             "Name", "Class", "Date Of Birth",
#             "Gender", "Phone Number", "Guardian's Name", "Address"
#         ]
#     )
#
#     update_options.grid(row=0, column=1, columnspan=4, sticky="w", padx=5, pady=5)
#
#     update_roll = c.CTkLabel(tabs, text="Roll Number ")
#     update_roll.grid(row=1, column=0, sticky="w", padx=5, pady=5)
#
#     update_entry_roll = c.CTkEntry(tabs, placeholder_text="of whose data is to be Updated")
#     update_entry_roll.grid(row=1, column=1, sticky="we", columnspan=2, padx=5, pady=5)
#
#     global dynamic_update_label
#     dynamic_update_label = c.CTkLabel(tabs, text="Name")
#     dynamic_update_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
#
#     global dynamic_update_entry
#     dynamic_update_entry = c.CTkEntry(tabs, placeholder_text="Updated Name")
#     dynamic_update_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)
#
#     enter_button = c.CTkButton(tabs, text="Enter", command=lambda: update_student_record(
#         update_entry_roll.get(), update_options.get(), dynamic_update_entry.get()
#     ))
#     enter_button.grid(row=3, column=1, padx=5, pady=5, columnspan=2, sticky="news")
#
#     # update student tab
#
#
# def create_insert_window(tab, table):
#     tab.destroy()
#
#     tab = c.CTkFrame(window)
#     tab.grid(row=0, column=1, columnspan=5, rowspan=4, sticky="news", padx=10, pady=10)
#     # Label Widgets -------
#     if table == "Student Table":
#         roll_no_label = c.CTkLabel(tab, text="Roll Number")  # primary key
#         roll_no_label.grid(row=0, column=0)
#
#         name_label = c.CTkLabel(tab, text="Name")
#         name_label.grid(row=0, column=1)
#
#         class_label = c.CTkLabel(tab, text="Class")
#         class_label.grid(row=0, column=2)
#
#         date_of_birth_label = c.CTkLabel(tab, text="Date Of Birth")
#         date_of_birth_label.grid(row=2, column=0)
#
#         gender_label = c.CTkLabel(tab, text="Gender")
#         gender_label.grid(row=2, column=1)
#
#         phone_number_label = c.CTkLabel(tab, text="Phone")
#         phone_number_label.grid(row=4, column=0)
#
#         guardian_name_label = c.CTkLabel(tab, text="Guardian's Name")
#         guardian_name_label.grid(row=4, column=1)
#
#         address_label = c.CTkLabel(tab, text="Address")
#         address_label.grid(row=6, column=0)
#
#         subjects_label = c.CTkLabel(tab, text="Opted Subjects")
#         subjects_label.grid(row=6, column=1)
#
#         # Entry Widgets --------
#
#         entry_roll_number = c.CTkEntry(tab, placeholder_text="roll number")
#         entry_roll_number.grid(row=1, column=0, padx=5, pady=5)
#
#         entry_name = c.CTkEntry(tab, placeholder_text="First Name")
#         entry_name.grid(row=1, column=1, padx=5, pady=5)
#
#         entry_class = c.CTkEntry(tab, placeholder_text="Class")
#         entry_class.grid(row=1, column=2, padx=5, pady=5)
#
#         entry_date = c.CTkEntry(tab, placeholder_text="YYYY-MM-DD")
#         entry_date.grid(row=3, column=0, padx=5, pady=5)
#
#         gender_value = tk.IntVar(value=0)
#         entry_male_gender = c.CTkRadioButton(tab, text="Male", variable=gender_value, value=0)
#         entry_male_gender.grid(row=3, column=1, padx=5, pady=5)
#         entry_female_gender = c.CTkRadioButton(tab, text="Female", variable=gender_value, value=1)
#         entry_female_gender.grid(row=3, column=2, padx=5, pady=5)
#
#         entry_phone_number = c.CTkEntry(tab, placeholder_text="Enter Phone number")
#         entry_phone_number.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
#
#         entry_guardian_name = c.CTkEntry(tab, placeholder_text="Enter Guardian's Name")
#         entry_guardian_name.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky="ew")
#
#         entry_address = c.CTkEntry(tab, placeholder_text="address")
#         entry_address.grid(row=7, column=0, padx=5, pady=5, sticky="news")
#
#         entry_subject_1 = c.CTkEntry(tab, placeholder_text="subject 1")
#         entry_subject_1.grid(row=7, column=1, padx=5, pady=5, sticky="news")
#
#         entry_subject_2 = c.CTkEntry(tab, placeholder_text="subject 2")
#         entry_subject_2.grid(row=7, column=2, padx=5, pady=5, sticky="news")
#
#         entry_subject_3 = c.CTkEntry(tab, placeholder_text="subject 3")
#         entry_subject_3.grid(row=8, column=1, padx=5, pady=5, sticky="news")
#
#         entry_subject_4 = c.CTkEntry(tab, placeholder_text="subject 4")
#         entry_subject_4.grid(row=8, column=2, padx=5, pady=5, sticky="news")
#
#         entry_subject_5 = c.CTkEntry(tab, placeholder_text="subject 5")
#         entry_subject_5.grid(row=9, column=1, padx=5, pady=5, sticky="news")
#
#         subjects = (entry_subject_1, entry_subject_2, entry_subject_3, entry_subject_4, entry_subject_5)
#
#         enter_button = c.CTkButton(tab, text="Enter",
#                                command=lambda: insert_student_record(
#                                    entry_roll_number.get(), entry_name.get(),
#                                    entry_class.get(), entry_date.get(),
#                                    gender_value.get(), entry_phone_number.get(),
#                                    entry_guardian_name.get(), entry_address.get(),
#                                    subjects)
#                                )
#         enter_button.grid(row=10, column=0, padx=50, pady=20, columnspan=3, sticky="news")
#
#     else:
#         roll_no = c.CTkLabel(tab, text="RollNo")  # primary key
#         roll_no.grid(row=0, column=0)
#
#         name = c.CTkLabel(tab, text="Name")
#         name.grid(row=1, column=0)
#
#         class_student = c.CTkLabel(tab, text="Class")
#         class_student.grid(row=2, column=0)
#
#         entry_roll_number = c.CTkEntry(tab, placeholder_text="Enter Roll Number")
#         entry_roll_number.grid(row=0, column=1, padx=5, pady=5)
#
#         entry_first_name = c.CTkEntry(tab, placeholder_text="First Name")
#         entry_first_name.grid(row=1, column=1, padx=5, pady=5)
#
#         entry_class = c.CTkEntry(tab, placeholder_text="Enter Class")
#         entry_class.grid(row=2, column=1, padx=5, pady=5)
#
#
# def select_update_value(choice, tab):
#     global dynamic_update_label
#     global dynamic_update_entry
#
#     dynamic_update_label.configure(text=choice)
#     dynamic_update_entry.destroy()
#
#     if choice == "Address":
#         dynamic_update_entry = c.CTkTextbox(tab)
#         dynamic_update_entry.grid(row=2, column=1, sticky="news", padx=5, pady=5, columnspan=2)
#
#     else:
#         dynamic_update_entry = c.CTkEntry(tab,
#                                           placeholder_text="Enter " + choice,
#                                           width=150)
#         dynamic_update_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)
#
#
# # SQL implementations
#
#
# # SQL implementations
#
# # main window


# Side Frame

# sidebar = c.CTkFrame(window)
# sidebar.grid(column=0, row=0, rowspan=7, columnspan=5, sticky="news", padx=10, pady=10)
# sidebar.bind('<Button-1>', remove_focus_sidebar)
#
# Title = c.CTkLabel(sidebar, text="SMS", height=10, width=20, font=c.CTkFont(size=30, weight="bold"))
# Title.grid(row=0, column=0, sticky="ew", padx=40, pady=40)
#
# select_table = c.CTkOptionMenu(sidebar, values=["Student Table", "Result Table"])
# select_table.grid(row=1, column=0, sticky="news", padx=10, pady=10)
#
# search_button = c.CTkButton(sidebar, text="SEARCH DATA", command=lambda: create_search_window(mainframe))
# search_button.grid(row=2, column=0, columnspan=2, sticky="news", padx=10, pady=10)
#
# insert_button = c.CTkButton(sidebar, text="INSERT DATA"
#                             , command=lambda: create_insert_window(mainframe, select_table.get()))
# insert_button.grid(row=3, column=0, sticky="news", padx=10, pady=10)
#
# update_button = c.CTkButton(sidebar, text="UPDATE DATA", command=lambda: create_update_window(mainframe))
# update_button.grid(row=4, column=0, columnspan=2, sticky="news", padx=10, pady=10)
#
# delete_button = c.CTkButton(sidebar, text="DELETE DATA", command=lambda: create_delete_window(mainframe))
# delete_button.grid(row=5, column=0, sticky="wens", padx=10, pady=10)
#
# mainframe = c.CTkFrame(window)
# mainframe.grid(row=0, column=6, columnspan=4, rowspan=4, sticky="news", padx=10, pady=10)

# create_search_window(mainframe)

window = c.CTk()
window.geometry("1024x575")
window.title("School Management System")

window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, uniform="uniformity")
window.columnconfigure([0, 1, 2, 3, 4, 5, 6], weight=1, uniform="uniformity")

fields_frame = c.CTkFrame(window)
fields_frame.grid(row=0, column=0, rowspan=7, columnspan=2, sticky="news", padx=10, pady=10)

roll_no_label = c.CTkLabel(fields_frame, text="Roll Number")  # primary key
roll_no_label.grid(row=0, column=0)

name_label = c.CTkLabel(fields_frame, text="Name")
name_label.grid(row=0, column=1)

class_label = c.CTkLabel(fields_frame, text="Class")
class_label.grid(row=0, column=2)

date_of_birth_label = c.CTkLabel(fields_frame, text="Date Of Birth")
date_of_birth_label.grid(row=2, column=0)

gender_label = c.CTkLabel(fields_frame, text="Gender")
gender_label.grid(row=2, column=1)

phone_number_label = c.CTkLabel(fields_frame, text="Phone")
phone_number_label.grid(row=4, column=0)

guardian_name_label = c.CTkLabel(fields_frame, text="Guardian's Name")
guardian_name_label.grid(row=4, column=1)

address_label = c.CTkLabel(fields_frame, text="Address")
address_label.grid(row=6, column=0)

subjects_label = c.CTkLabel(fields_frame, text="Opted Subjects")
subjects_label.grid(row=6, column=1)

# Entry Widgets --------

entry_roll_number = c.CTkEntry(fields_frame, placeholder_text="roll number")
entry_roll_number.grid(row=1, column=0, padx=5, pady=5)

entry_name = c.CTkEntry(fields_frame, placeholder_text="First Name")
entry_name.grid(row=1, column=1, padx=5, pady=5)

entry_class = c.CTkEntry(fields_frame, placeholder_text="Class")
entry_class.grid(row=1, column=2, padx=5, pady=5)

entry_date = c.CTkEntry(fields_frame, placeholder_text="YYYY-MM-DD")
entry_date.grid(row=3, column=0, padx=5, pady=5)

gender_value = tk.IntVar(value=0)
entry_male_gender = c.CTkRadioButton(fields_frame, text="Male", variable=gender_value, value=0)
entry_male_gender.grid(row=3, column=1, padx=5, pady=5)
entry_female_gender = c.CTkRadioButton(fields_frame, text="Female", variable=gender_value, value=1)
entry_female_gender.grid(row=3, column=2, padx=5, pady=5)

entry_phone_number = c.CTkEntry(fields_frame, placeholder_text="Enter Phone number")
entry_phone_number.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

entry_guardian_name = c.CTkEntry(fields_frame, placeholder_text="Enter Guardian's Name")
entry_guardian_name.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

entry_address = c.CTkEntry(fields_frame, placeholder_text="address")
entry_address.grid(row=7, column=0, padx=5, pady=5, sticky="news")

entry_subject_1 = c.CTkEntry(fields_frame, placeholder_text="subject 1")
entry_subject_1.grid(row=7, column=1, padx=5, pady=5, sticky="news")

entry_subject_2 = c.CTkEntry(fields_frame, placeholder_text="subject 2")
entry_subject_2.grid(row=7, column=2, padx=5, pady=5, sticky="news")

entry_subject_3 = c.CTkEntry(fields_frame, placeholder_text="subject 3")
entry_subject_3.grid(row=8, column=1, padx=5, pady=5, sticky="news")

entry_subject_4 = c.CTkEntry(fields_frame, placeholder_text="subject 4")
entry_subject_4.grid(row=8, column=2, padx=5, pady=5, sticky="news")

entry_subject_5 = c.CTkEntry(fields_frame, placeholder_text="subject 5")
entry_subject_5.grid(row=9, column=1, padx=5, pady=5, sticky="news")


window.mainloop()
