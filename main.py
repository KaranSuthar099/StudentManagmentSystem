import tkinter as tk

import customtkinter as c

c.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

flagFirstRun = 0
value_check = 0


def removeFocusSidebar(event):
    # Remove focus from the widget that currently has focus
    sidebar.focus()


def removeFocusSearchFrame(event):
    # Remove focus from the widget that currently has focus
    SearchFrame.focus()


def removeFocustabs(event):
    # Remove focus from the widget that currently has focus
    dynamictabs.focus_set()


def SelectUpdateValue(choice):
    dynamicLabel.configure(text="Enter " + choice)
    global DynamicWidget
    DynamicWidget.destroy()

    if choice == "Name":
        DynamicWidget = c.CTkEntry(dynamictabs.tab("Update Student Data"), placeholder_text="Updated Name")
        DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Class":
        DynamicWidget = c.CTkEntry(dynamictabs.tab("Update Student Data"), placeholder_text="Updated Class")
        DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Date Of Birth":
        dynamicLabel.configure(text="Enter " + choice)
        DynamicWidget = c.CTkEntry(dynamictabs.tab("Update Student Data"), width=200,
                                   placeholder_text="in format (YYYY/MM/DD)")
        DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Gender":
        DynamicWidget = c.CTkOptionMenu(dynamictabs.tab("Update Student Data"), values=["Male", "Female"])
        DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Phone Number":
        DynamicWidget = c.CTkEntry(dynamictabs.tab("Update Student Data"), placeholder_text="Updated Phone Number")
        DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Guardian's Name":
        DynamicWidget = c.CTkEntry(dynamictabs.tab("Update Student Data"), placeholder_text="Updated Guardian's Name")
        DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Address":
        DynamicWidget = c.CTkTextbox(dynamictabs.tab("Update Student Data"), width=30)
        DynamicWidget.grid(row=2, column=1, sticky="news", padx=5, pady=5, columnspan=2)


# def SelectTabview(choice, dynamictabs):
#     dynamictabs.destroy()
#
#     if choice == "Student Table":
#         dynamictabs = c.CTkTabview(window, corner_radius=20, width=400)
#
#         dynamictabs.add("Insert Student Data")
#         dynamictabs.add("Update Student Data")
#         dynamictabs.add("Delete Student Data")
#
#         # tabs.bind('<Button-1>', removeFocustabs)
#
#         dynamictabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)
#
#         RollNo = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="RollNo")  # primary key
#         RollNo.grid(row=0, column=1)
#
#         Name = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Name")
#         Name.grid(row=1, column=1)
#
#         Class = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Class")
#         Class.grid(row=2, column=1)
#
#         DateOfBirth = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="DateOfBirth")
#         DateOfBirth.grid(row=3, column=1)
#
#         Gender = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Gender")
#         Gender.grid(row=4, column=1)
#
#         PhoneNumber = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Phone")
#         PhoneNumber.grid(row=5, column=1)
#
#         GuardianName = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="GuardianName")
#         GuardianName.grid(row=6, column=1)
#
#         Address = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Address")
#         Address.grid(row=7, column=1)
#
#         EntryRollNumber = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Roll Number")
#         EntryRollNumber.grid(row=0, column=2, padx=5, pady=5)
#
#         EntryFirstName = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="First Name")
#         EntryFirstName.grid(row=1, column=2, padx=5, pady=5)
#         EntrySecondName = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Last Name")
#         EntrySecondName.grid(row=1, column=3, padx=5, pady=5)
#
#         EntryClass = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Class")
#         EntryClass.grid(row=2, column=2, padx=5, pady=5)
#
#         EntryDay = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Day")
#         EntryDay.grid(row=3, column=2, padx=5, pady=5)
#         EntryMonth = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Month")
#         EntryMonth.grid(row=3, column=3, padx=5, pady=5)
#         EntryYear = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Year")
#         EntryYear.grid(row=3, column=4, padx=5, pady=5)
#
#         RadioVal = tk.IntVar(value=0)
#         EntryMaleGender = c.CTkRadioButton(dynamictabs.tab("Insert Student Data"), text="Male", variable=RadioVal,
#                                            value=0)
#         EntryMaleGender.grid(row=4, column=2, padx=5, pady=5)
#         EntryFemaleGender = c.CTkRadioButton(dynamictabs.tab("Insert Student Data"), text="Female", variable=RadioVal,
#                                              value=1)
#         EntryFemaleGender.grid(row=4, column=3, padx=5, pady=5)
#
#         EntryPhoneNumber = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Phone number")
#         EntryPhoneNumber.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="ew")
#
#         EntryGuardianName = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Guardian's Name")
#         EntryGuardianName.grid(row=6, column=2, padx=5, pady=5, columnspan=2, sticky="ew")
#
#         EntryAddress = c.CTkTextbox(dynamictabs.tab("Insert Student Data"), width=30)
#         EntryAddress.grid(row=7, column=2, padx=5, pady=5, columnspan=2, sticky="news")
#
#         EnterButton = c.CTkButton(dynamictabs.tab("Insert Student Data"), text="Enter")
#         EnterButton.grid(row=8, column=2, padx=5, pady=30, columnspan=2, sticky="news")
#
#         # update student tab
#
#         deleteLabel = c.CTkLabel(dynamictabs.tab("Update Student Data"), text="You want to Update ")
#         deleteLabel.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#
#         DeleteOption = c.CTkOptionMenu(dynamictabs.tab("Update Student Data"), width=400, command=SelectUpdateValue
#                                        , values=["Name", "Class",
#                                                  "Date Of Birth", "Gender",
#                                                  "Phone Number", "Guardian's Name",
#                                                  "Address"])
#         DeleteOption.grid(row=0, column=1, columnspan=4, sticky="w", padx=5, pady=5)
#
#         updateRoll = c.CTkLabel(dynamictabs.tab("Update Student Data"), text="Roll Number ")
#         updateRoll.grid(row=1, column=0, sticky="w", padx=5, pady=5)
#
#         updateEntryRoll = c.CTkEntry(dynamictabs.tab("Update Student Data"),
#                                      placeholder_text="of whose data is to be Updated")
#         updateEntryRoll.grid(row=1, column=1, sticky="we", columnspan=2, padx=5, pady=5)
#
#         dynamicLabel = c.CTkLabel(dynamictabs.tab("Update Student Data"), text="Name")
#         dynamicLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)
#
#         DynamicWidget = c.CTkEntry(dynamictabs.tab("Update Student Data"), placeholder_text="Updated Name")
#         DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
#
#         EnterButton = c.CTkButton(dynamictabs.tab("Update Student Data"), text="Enter")
#         EnterButton.grid(row=3, column=1, padx=5, pady=30, columnspan=2, sticky="news")
#
#         # update student tab
#
#         deleteRollLabel = c.CTkLabel(dynamictabs.tab("Delete Student Data"), text="Roll Number ", width=150)
#         deleteRollLabel.grid(row=0, column=0, sticky="news", padx=5, pady=5)
#
#         deleteEntryRoll = c.CTkEntry(dynamictabs.tab("Delete Student Data"), width=300,
#                                      placeholder_text="of whose data is to be "
#                                                       "Deleted")
#         deleteEntryRoll.grid(row=0, column=1, columnspan=2, sticky="news", padx=5, pady=5)
#
#         EnterButtonDelete = c.CTkButton(dynamictabs.tab("Delete Student Data"), text="Enter")
#         EnterButtonDelete.grid(row=1, column=1, columnspan=2, padx=10, pady=30, sticky="news")

def SelectUpdateValue(choice):
    dynamicLabel.configure(text="Enter " + choice)
    global DynamicWidget
    DynamicWidget.destroy()


window = c.CTk()
window.geometry("1280x720")
window.title("School Management System")

window.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, uniform="uniform columns")
window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="uniform rows")

# Side Frame
sidebar = c.CTkFrame(window, corner_radius=20, width=120)
sidebar.grid(column=0, row=0, rowspan=7, sticky="news", padx=10, pady=10)

searchSelectTable = c.CTkOptionMenu(sidebar, values=["Student Table", "Result Table"], command=SelectUpdateValue)
searchSelectTable.grid(row=1, column=0, sticky="wen", padx=10, pady=10)

sidebar.bind('<Button-1>', removeFocusSidebar)

# Side Frame

# Search Frame

SearchFrame = c.CTkFrame(window, corner_radius=20)
SearchFrame.bind('<Button-1>', removeFocusSearchFrame)

SearchFrame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="uniform")
SearchFrame.rowconfigure((0, 1, 2), weight=1, uniform="uniform")
SearchFrame.grid(row=0, column=5, rowspan=7, columnspan=3, sticky="news", padx=10, pady=10)

SearchBar = c.CTkEntry(SearchFrame, placeholder_text="S e a r c h", width=200)
SearchBar.grid(row=0, column=0, sticky="sew", padx=10, pady=10, columnspan=2)

SearchButton = c.CTkButton(SearchFrame, text="Search")
SearchButton.grid(row=0, column=2, sticky="sew", padx=[5, 5], pady=10)

searchSelectTable = c.CTkOptionMenu(SearchFrame, values=["Student Table", "Result Table"])
searchSelectTable.grid(row=1, column=0, sticky="wen", padx=10, pady=10)

# Frame Search Data

Title = c.CTkLabel(sidebar, text="SMS", height=10, width=20, font=c.CTkFont(size=30, weight="bold"))
Title.grid(row=0, column=0, sticky="ew", padx=40, pady=40)
# label title

dynamictabs = c.CTkTabview(window, corner_radius=20, width=400)

dynamictabs.add("Insert Student Data")
dynamictabs.add("Update Student Data")
dynamictabs.add("Delete Student Data")

# tabs.bind('<Button-1>', removeFocustabs)

dynamictabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

RollNo = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="RollNo")  # primary key
RollNo.grid(row=0, column=1)

Name = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Name")
Name.grid(row=1, column=1)

Class = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Class")
Class.grid(row=2, column=1)

DateOfBirth = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="DateOfBirth")
DateOfBirth.grid(row=3, column=1)

Gender = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Gender")
Gender.grid(row=4, column=1)

PhoneNumber = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Phone")
PhoneNumber.grid(row=5, column=1)

GuardianName = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="GuardianName")
GuardianName.grid(row=6, column=1)

Address = c.CTkLabel(dynamictabs.tab("Insert Student Data"), text="Address")
Address.grid(row=7, column=1)

EntryRollNumber = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Roll Number")
EntryRollNumber.grid(row=0, column=2, padx=5, pady=5)

EntryFirstName = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="First Name")
EntryFirstName.grid(row=1, column=2, padx=5, pady=5)
EntrySecondName = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Last Name")
EntrySecondName.grid(row=1, column=3, padx=5, pady=5)

EntryClass = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Class")
EntryClass.grid(row=2, column=2, padx=5, pady=5)

EntryDay = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Day")
EntryDay.grid(row=3, column=2, padx=5, pady=5)
EntryMonth = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Month")
EntryMonth.grid(row=3, column=3, padx=5, pady=5)
EntryYear = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Year")
EntryYear.grid(row=3, column=4, padx=5, pady=5)

RadioVal = tk.IntVar(value=0)
EntryMaleGender = c.CTkRadioButton(dynamictabs.tab("Insert Student Data"), text="Male", variable=RadioVal, value=0)
EntryMaleGender.grid(row=4, column=2, padx=5, pady=5)
EntryFemaleGender = c.CTkRadioButton(dynamictabs.tab("Insert Student Data"), text="Female", variable=RadioVal, value=1)
EntryFemaleGender.grid(row=4, column=3, padx=5, pady=5)

EntryPhoneNumber = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Phone number")
EntryPhoneNumber.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="ew")

EntryGuardianName = c.CTkEntry(dynamictabs.tab("Insert Student Data"), placeholder_text="Enter Guardian's Name")
EntryGuardianName.grid(row=6, column=2, padx=5, pady=5, columnspan=2, sticky="ew")

EntryAddress = c.CTkTextbox(dynamictabs.tab("Insert Student Data"), width=30)
EntryAddress.grid(row=7, column=2, padx=5, pady=5, columnspan=2, sticky="news")

EnterButton = c.CTkButton(dynamictabs.tab("Insert Student Data"), text="Enter")
EnterButton.grid(row=8, column=2, padx=5, pady=30, columnspan=2, sticky="news")

# update student tab

deleteLabel = c.CTkLabel(dynamictabs.tab("Update Student Data"), text="You want to Update ")
deleteLabel.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

DeleteOption = c.CTkOptionMenu(dynamictabs.tab("Update Student Data"), width=400, command=SelectUpdateValue
                               , values=["Name", "Class",
                                         "Date Of Birth", "Gender",
                                         "Phone Number", "Guardian's Name",
                                         "Address"])
DeleteOption.grid(row=0, column=1, columnspan=4, sticky="w", padx=5, pady=5)

updateRoll = c.CTkLabel(dynamictabs.tab("Update Student Data"), text="Roll Number ")
updateRoll.grid(row=1, column=0, sticky="w", padx=5, pady=5)

updateEntryRoll = c.CTkEntry(dynamictabs.tab("Update Student Data"), placeholder_text="of whose data is to be Updated")
updateEntryRoll.grid(row=1, column=1, sticky="we", columnspan=2, padx=5, pady=5)

dynamicLabel = c.CTkLabel(dynamictabs.tab("Update Student Data"), text="Name")
dynamicLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)

DynamicWidget = c.CTkEntry(dynamictabs.tab("Update Student Data"), placeholder_text="Updated Name")
DynamicWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)

EnterButton = c.CTkButton(dynamictabs.tab("Update Student Data"), text="Enter")
EnterButton.grid(row=3, column=1, padx=5, pady=30, columnspan=2, sticky="news")

# update student tab

deleteRollLabel = c.CTkLabel(dynamictabs.tab("Delete Student Data"), text="Roll Number ", width=150)
deleteRollLabel.grid(row=0, column=0, sticky="news", padx=5, pady=5)

deleteEntryRoll = c.CTkEntry(dynamictabs.tab("Delete Student Data"), width=300,
                             placeholder_text="of whose data is to be "
                                              "Deleted")
deleteEntryRoll.grid(row=0, column=1, columnspan=2, sticky="news", padx=5, pady=5)

EnterButtonDelete = c.CTkButton(dynamictabs.tab("Delete Student Data"), text="Enter")
EnterButtonDelete.grid(row=1, column=1, columnspan=2, padx=10, pady=30, sticky="news")

window.mainloop()
