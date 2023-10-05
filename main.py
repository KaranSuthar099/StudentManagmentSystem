import tkinter as tk
import mysql.connector as sql
import customtkinter as c


c.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


flagFirstRun = 0
value_check = 0
var_row = 0
current_row = 4

def remove_focus_sidebar(_):
    # Remove focus from the widget that currently has focus
    sidebar.focus()

# def remove_focus_search_frame(_):
#     SearchFrame.focus()

def remove_focus_tabs(_):
    Tabs.focus_set()

def insert_student_record(roll, name, class_number, date, gender, phone_number, guardian_name, address, subjects ):

    if gender == 0:
        gender = "Male"
    else:
        gender = "Female"
    global subjects_str

    subjects_str = ""
    for i in subjects:
        i = i.get()
        subjects_str += str(i) + ","

    query = "INSERT INTO STUDENT_RECORDS (roll_number, name, class, Date_Of_Birth, Gender, Phone_Number, Guardians_Name, Address, Subjects)" \
            " VALUES ({}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}' )".format(str(roll), name,
                                                                              str(class_number), date, gender,
                                                                              str(phone_number), guardian_name,
                                                                              address, subjects_str)
    try:
        cursor.execute(query)
        mydb.commit()
        print("data entry success")
    except Exception as e:
        print("ERROR!!! ", e)

def update_student_record(roll, field, updated_value):
    query = "update student_records set {} = {} where Roll_Number={}".format(field, updated_value, roll)
    try:
        cursor.execute(query)
        mydb.commit()
        print("data update success")
    except Exception as e:
        print("ERROR!!! ", e)

def delete_student_record(roll):
    query = "delete from student_records where roll_number = {}".format(roll)
    try:
        cursor.execute(query)
        mydb.commit()
        print("data delete success")
    except Exception as e:
        print("ERROR!!! ", e)

def create_delete_window(tab):
    delete_roll_label = c.CTkLabel(Tabs.tab(tab), text="Roll Number ", width=150)
    delete_roll_label.grid(row=0, column=0, sticky="news", padx=5, pady=5)

    delete_entry_roll = c.CTkEntry(Tabs.tab(tab), width=300, placeholder_text="of whose data is to be Deleted")
    delete_entry_roll.grid(row=0, column=1, columnspan=2, sticky="news", padx=5, pady=5)

    enter_button_delete = c.CTkButton(Tabs.tab(tab), text="Enter", command= lambda: delete_student_record(
        delete_entry_roll.get()
    ))
    enter_button_delete.grid(row=1, column=1, columnspan=2, padx=10, pady=30, sticky="news")


def create_update_window(tab):
    # update student tab

    update_label = c.CTkLabel(Tabs.tab(tab), text="You want to Update ")
    update_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    update_options = c.CTkOptionMenu(
        Tabs.tab(tab),
        width=400,
        command=select_update_value,
        values=[
            "Name", "Class", "Date Of Birth",
            "Gender", "Phone Number", "Guardian's Name", "Address"
        ]
    )

    update_options.grid(row=0, column=1, columnspan=4, sticky="w", padx=5, pady=5)

    update_roll = c.CTkLabel(Tabs.tab(tab), text="Roll Number ")
    update_roll.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    update_entry_roll = c.CTkEntry(Tabs.tab(tab), placeholder_text="of whose data is to be Updated")
    update_entry_roll.grid(row=1, column=1, sticky="we", columnspan=2, padx=5, pady=5)

    global dynamic_update_label
    dynamic_update_label = c.CTkLabel(Tabs.tab(tab), text="Name")
    dynamic_update_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    global dynamic_update_entry
    dynamic_update_entry = c.CTkEntry(Tabs.tab(tab), placeholder_text="Updated Name")
    dynamic_update_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    enter_button = c.CTkButton(Tabs.tab(tab), text="Enter", command=lambda: update_student_record(
        update_entry_roll.get(), update_options.get(), dynamic_update_entry.get()
    ))
    enter_button.grid(row=3, column=1, padx=5, pady=30, columnspan=2, sticky="news")

    # update student tab


def create_insert_window(tab):

    # Label Widgets -------

    roll_no_label = c.CTkLabel(Tabs.tab(tab), text="Roll Number")  # primary key
    roll_no_label.grid(row=0, column=0)

    name_label = c.CTkLabel(Tabs.tab(tab), text="Name")
    name_label.grid(row=0, column=1)

    class_label = c.CTkLabel(Tabs.tab(tab), text="Class")
    class_label.grid(row=0, column=2)

    date_of_birth_label = c.CTkLabel(Tabs.tab(tab), text="Date Of Birth")
    date_of_birth_label.grid(row=2, column=0)

    gender_label = c.CTkLabel(Tabs.tab(tab), text="Gender")
    gender_label.grid(row=2, column=1)

    phone_number_label = c.CTkLabel(Tabs.tab(tab), text="Phone")
    phone_number_label.grid(row=4, column=0)

    guardian_name_label = c.CTkLabel(Tabs.tab(tab), text="Guardian's Name")
    guardian_name_label.grid(row=4, column=1)

    address_label = c.CTkLabel(Tabs.tab(tab), text="Address")
    address_label.grid(row=6, column=0)

    subjects_label = c.CTkLabel(Tabs.tab(tab), text="Opted Subjects")
    subjects_label.grid(row=6, column=1)

# Entry Widgets --------

    entry_roll_number = c.CTkEntry(Tabs.tab(tab), placeholder_text="roll number")
    entry_roll_number.grid(row=1, column=0, padx=5, pady=5)

    entry_name = c.CTkEntry(Tabs.tab(tab), placeholder_text="First Name")
    entry_name.grid(row=1, column=1, padx=5, pady=5)

    entry_class = c.CTkEntry(Tabs.tab(tab), placeholder_text="Class")
    entry_class.grid(row=1, column=2, padx=5, pady=5)

    entry_date = c.CTkEntry(Tabs.tab(tab), placeholder_text="YYYY-MM-DD")
    entry_date.grid(row=3, column=0, padx=5, pady=5)

    gender_value = tk.IntVar(value=0)
    entry_male_gender = c.CTkRadioButton(Tabs.tab(tab), text="Male", variable=gender_value, value=0)
    entry_male_gender.grid(row=3, column=1, padx=5, pady=5)
    entry_female_gender = c.CTkRadioButton(Tabs.tab(tab), text="Female", variable=gender_value, value=1)
    entry_female_gender.grid(row=3, column=2, padx=5, pady=5)

    entry_phone_number = c.CTkEntry(Tabs.tab(tab), placeholder_text="Enter Phone number")
    entry_phone_number.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

    entry_guardian_name = c.CTkEntry(Tabs.tab(tab), placeholder_text="Enter Guardian's Name")
    entry_guardian_name.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

    entry_address = c.CTkEntry(Tabs.tab(tab), placeholder_text="address")
    entry_address.grid(row=7, column=0, padx=5, pady=5, sticky="news")

    entry_subject_1 = c.CTkEntry(Tabs.tab(tab), placeholder_text="subject 1")
    entry_subject_1.grid(row=7, column=1, padx=5, pady=5, sticky="news")

    entry_subject_2 = c.CTkEntry(Tabs.tab(tab), placeholder_text="subject 2")
    entry_subject_2.grid(row=7, column=2, padx=5, pady=5, sticky="news")

    entry_subject_3 = c.CTkEntry(Tabs.tab(tab), placeholder_text="subject 3")
    entry_subject_3.grid(row=8, column=1, padx=5, pady=5, sticky="news")

    entry_subject_4 = c.CTkEntry(Tabs.tab(tab), placeholder_text="subject 4")
    entry_subject_4.grid(row=8, column=2, padx=5, pady=5, sticky="news")

    entry_subject_5 = c.CTkEntry(Tabs.tab(tab), placeholder_text="subject 5")
    entry_subject_5.grid(row=9, column=1, padx=5, pady=5, sticky="news")

    subjects = (entry_subject_1, entry_subject_2, entry_subject_3, entry_subject_4, entry_subject_5)

    enter_button = c.CTkButton(Tabs.tab(tab), text="Enter",
                               command=lambda: insert_student_record(
                                   entry_roll_number.get(), entry_name.get(),
                                   entry_class.get(), entry_date.get(),
                                   gender_value.get(), entry_phone_number.get(),
                                   entry_guardian_name.get(), entry_address.get(),
                                   subjects)
                               )
    enter_button.grid(row=10, column=0, padx=50, pady=20, columnspan=3, sticky="news")


def select_update_value(choice):
    global dynamic_update_label
    global dynamic_update_entry

    dynamic_update_label.configure(text=choice)
    dynamic_update_entry.destroy()

    if choice == "Address":
        dynamic_update_entry = c.CTkTextbox(Tabs.tab("Update Student Data"), width=30)
        dynamic_update_entry.grid(row=2, column=1, sticky="news", padx=5, pady=5, columnspan=2)

    else:
        dynamic_update_entry = c.CTkEntry(Tabs.tab("Update Student Data"),
                                          placeholder_text="Enter " + choice,
                                          width=150)
        dynamic_update_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# result table code in HERE
def SelectTableMainFrame(choice):
    global Tabs
    Tabs.destroy()

    if choice == "Student Table":
        Tabs = c.CTkTabview(window, corner_radius=20, width=400)

        Tabs.add("Insert Student Data")
        Tabs.add("Update Student Data")
        Tabs.add("Delete Student Data")

        Tabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

        create_insert_window("Insert Student Data")
        create_update_window("Update Student Data")
        create_delete_window("Delete Student Data")

    elif choice == "Result Table":

        Tabs = c.CTkTabview(window, corner_radius=20, width=400)

        Tabs.add("Insert Student Result Data")
        Tabs.add("Update Student Result Data")
        Tabs.add("Delete Student Result Data")

        Tabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

        roll_no = c.CTkLabel(Tabs.tab("Insert Student Result Data"), text="RollNo")  # primary key
        roll_no.grid(row=0, column=0)

        name = c.CTkLabel(Tabs.tab("Insert Student Result Data"), text="Name")
        name.grid(row=1, column=0)

        class_student = c.CTkLabel(Tabs.tab("Insert Student Result Data"), text="Class")
        class_student.grid(row=2, column=0)

        entry_roll_number = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="Enter Roll Number")
        entry_roll_number.grid(row=0, column=1, padx=5, pady=5)

        entry_first_name = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="First Name")
        entry_first_name.grid(row=1, column=1, padx=5, pady=5)
        entry_second_name = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="Last Name")
        entry_second_name.grid(row=1, column=2, padx=5, pady=5)

        entry_class = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="Enter Class")
        entry_class.grid(row=2, column=1, padx=5, pady=5)


# SQL implementations

mydb = sql.connect(host="localhost", user="root", passwd="root")  # Establishing SQL connection

cursor = mydb.cursor()  # Creating Cursor object


cursor.execute("CREATE DATABASE IF NOT EXISTS STUDENT_MANAGEMENT_SYSTEM")
cursor.execute("USE STUDENT_MANAGEMENT_SYSTEM")
cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENT_RECORDS (
    Roll_Number INT PRIMARY KEY,
    Name VARCHAR(50),
    Class INT,
    Date_Of_Birth DATE,
    Gender ENUM('Male', 'Female'),
    Phone_Number BIGINT,
    Guardians_Name VARCHAR(50),
    Address VARCHAR(255), 
    Subjects VARCHAR(255)
);
''')

cursor.execute("""CREATE TABLE IF NOT EXISTS Subjects (roll_number int , subject_one varchar(20) ,
                        subject_two varchar(20), subject_three varchar(20), 
                        subject_four varchar(20), subject_five varchar(20)) """)

# SQL implementations

# main window

window = c.CTk()
window.geometry("1280x720")
window.title("School Management System")

window.columnconfigure(0, weight=1, uniform="uniform columns")
window.columnconfigure(1, weight=1, uniform="uniform columns")
window.columnconfigure(2, weight=1, uniform="uniform columns")
window.columnconfigure(3, weight=1, uniform="uniform columns")
window.columnconfigure(4, weight=1, uniform="uniform columns")
window.columnconfigure(5, weight=1, uniform="uniform columns")

window.rowconfigure(0, weight=1, uniform="uniform rows")
window.rowconfigure(1, weight=1, uniform="uniform rows")
window.rowconfigure(2, weight=1, uniform="uniform rows")
window.rowconfigure(3, weight=1, uniform="uniform rows")

# Side Frame

sidebar = c.CTkFrame(window, corner_radius=20, width=120)
sidebar.grid(column=0, row=0, rowspan=7, columnspan=2, sticky="news", padx=10, pady=10)

sideFrameSelectTable = c.CTkOptionMenu(sidebar, values=["Student Table", "Result Table"], command=SelectTableMainFrame)
sideFrameSelectTable.grid(row=1, column=0, sticky="wen", padx=10, pady=10)

sidebar.bind('<Button-1>', remove_focus_sidebar)

Title = c.CTkLabel(sidebar, text="SMS", height=10, width=20, font=c.CTkFont(size=30, weight="bold"))
Title.grid(row=0, column=0, sticky="ew", padx=40, pady=40)

data_button = c.CTkButton(sidebar, text="INSERT DATA")
data_button.grid(row=2, column=0, sticky="wen", padx=10, pady=10)

insert_button = c.CTkButton(sidebar, text="INSERT DATA")
insert_button.grid(row=3, column=0, sticky="wen", padx=10, pady=10)

update_button = c.CTkButton(sidebar, text="INSERT DATA")
update_button.grid(row=4, column=0, sticky="wen", padx=10, pady=10)

delete_button = c.CTkButton(sidebar, text="INSERT DATA")
delete_button.grid(row=5, column=0, sticky="wen", padx=10, pady=10)


# Side Frame

# # Search Frame
#
# SearchFrame = c.CTkFrame(window, corner_radius=20)
# SearchFrame.bind('<Button-1>', remove_focus_search_frame)
# SearchFrame.rowconfigure(0, weight=1, uniform="uniform")
# SearchFrame.rowconfigure(1, weight=1, uniform="uniform")
# SearchFrame.rowconfigure(2, weight=1, uniform="uniform")
# SearchFrame.rowconfigure(3, weight=1, uniform="uniform")
#
# SearchFrame.grid(row=0, column=5, rowspan=7, columnspan=3, sticky="news", padx=10, pady=10)
# SearchBar = c.CTkEntry(SearchFrame, placeholder_text="S e a r c h", width=200)
#
# SearchBar.grid(row=0, column=0, sticky="sew", padx=10, pady=10, columnspan=2)
# SearchButton = c.CTkButton(SearchFrame, text="Search")
#
# SearchButton.grid(row=0, column=2, sticky="sew", padx=[5, 5], pady=10)
# searchSelectTable = c.CTkOptionMenu(SearchFrame, values=["Student Table", "Result Table"])
#
# searchSelectTable.grid(row=1, column=0, sticky="wen", padx=10, pady=10)
# # Frame Search Data

Tabs = c.CTkTabview(window, corner_radius=20, width=400)
Tabs.add("Insert Student Data")
Tabs.add("Update Student Data")
Tabs.add("Delete Student Data")

Tabs.grid(row=0, column=2, columnspan=4, rowspan=4, sticky="news", padx=10, pady=10)

create_insert_window("Insert Student Data")
create_update_window("Update Student Data")
create_delete_window("Delete Student Data")

window.mainloop()
