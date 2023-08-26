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
    Tabs.focus_set()

def createDeleteWindowWidgets(tab):
    deleteRollLabel = c.CTkLabel(Tabs.tab(tab), text="Roll Number ", width=150)
    deleteRollLabel.grid(row=0, column=0, sticky="news", padx=5, pady=5)

    deleteEntryRoll = c.CTkEntry(Tabs.tab(tab), width=300,placeholder_text="of whose data is to be Deleted")
    deleteEntryRoll.grid(row=0, column=1, columnspan=2, sticky="news", padx=5, pady=5)

    EnterButtonDelete = c.CTkButton(Tabs.tab(tab), text="Enter")
    EnterButtonDelete.grid(row=1, column=1, columnspan=2, padx=10, pady=30, sticky="news")

def createUpdateWindowWidgets(tab):
    # update student tab

    UpdateLabel = c.CTkLabel(Tabs.tab(tab), text="You want to Update ")
    UpdateLabel.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

    UpdateOptions = c.CTkOptionMenu(Tabs.tab(tab), width=400, command=SelectUpdateValue
                                   , values=["Name", "Class",
                                             "Date Of Birth", "Gender",
                                             "Phone Number", "Guardian's Name",
                                             "Address"])
    UpdateOptions.grid(row=0, column=1, columnspan=4, sticky="w", padx=5, pady=5)

    updateRoll = c.CTkLabel(Tabs.tab(tab), text="Roll Number ")
    updateRoll.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    updateEntryRoll = c.CTkEntry(Tabs.tab(tab), placeholder_text="of whose data is to be Updated")
    updateEntryRoll.grid(row=1, column=1, sticky="we", columnspan=2, padx=5, pady=5)

    global DynamicUpdateLabel
    DynamicUpdateLabel = c.CTkLabel(Tabs.tab(tab), text="Name")
    DynamicUpdateLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    global DynamicUpdateWidget
    DynamicUpdateWidget = c.CTkEntry(Tabs.tab(tab), placeholder_text="Updated Name")
    DynamicUpdateWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    EnterButton = c.CTkButton(Tabs.tab(tab), text="Enter")
    EnterButton.grid(row=3, column=1, padx=5, pady=30, columnspan=2, sticky="news")

    # update student tab

def create_insert_window_widgets(tab):
    RollNo = c.CTkLabel(Tabs.tab(tab), text="RollNo")  # primary key
    RollNo.grid(row=0, column=1)

    Name = c.CTkLabel(Tabs.tab(tab), text="Name")
    Name.grid(row=1, column=1)

    Class = c.CTkLabel(Tabs.tab(tab), text="Class")
    Class.grid(row=2, column=1)

    DateOfBirth = c.CTkLabel(Tabs.tab(tab), text="DateOfBirth")
    DateOfBirth.grid(row=3, column=1)

    Gender = c.CTkLabel(Tabs.tab(tab), text="Gender")
    Gender.grid(row=4, column=1)

    PhoneNumber = c.CTkLabel(Tabs.tab(tab), text="Phone")
    PhoneNumber.grid(row=5, column=1)

    GuardianName = c.CTkLabel(Tabs.tab(tab), text="GuardianName")
    GuardianName.grid(row=6, column=1)

    Address = c.CTkLabel(Tabs.tab(tab), text="Address")
    Address.grid(row=7, column=1)

    EntryRollNumber = c.CTkEntry(Tabs.tab(tab), placeholder_text="Enter Roll Number")
    EntryRollNumber.grid(row=0, column=2, padx=5, pady=5)

    EntryFirstName = c.CTkEntry(Tabs.tab(tab), placeholder_text="First Name")
    EntryFirstName.grid(row=1, column=2, padx=5, pady=5)
    EntrySecondName = c.CTkEntry(Tabs.tab(tab), placeholder_text="Last Name")
    EntrySecondName.grid(row=1, column=3, padx=5, pady=5)

    EntryClass = c.CTkEntry(Tabs.tab(tab), placeholder_text="Enter Class")
    EntryClass.grid(row=2, column=2, padx=5, pady=5)

    EntryDay = c.CTkEntry(Tabs.tab(tab), placeholder_text="Day")
    EntryDay.grid(row=3, column=2, padx=5, pady=5)
    EntryMonth = c.CTkEntry(Tabs.tab(tab), placeholder_text="Month")
    EntryMonth.grid(row=3, column=3, padx=5, pady=5)
    EntryYear = c.CTkEntry(Tabs.tab(tab), placeholder_text="Year")
    EntryYear.grid(row=3, column=4, padx=5, pady=5)

    RadioVal = tk.IntVar(value=0)
    EntryMaleGender = c.CTkRadioButton(Tabs.tab(tab), text="Male", variable=RadioVal, value=0)
    EntryMaleGender.grid(row=4, column=2, padx=5, pady=5)
    EntryFemaleGender = c.CTkRadioButton(Tabs.tab(tab), text="Female", variable=RadioVal, value=1)
    EntryFemaleGender.grid(row=4, column=3, padx=5, pady=5)

    EntryPhoneNumber = c.CTkEntry(Tabs.tab(tab), placeholder_text="Enter Phone number")
    EntryPhoneNumber.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="ew")

    EntryGuardianName = c.CTkEntry(Tabs.tab(tab), placeholder_text="Enter Guardian's Name")
    EntryGuardianName.grid(row=6, column=2, padx=5, pady=5, columnspan=2, sticky="ew")

    EntryAddress = c.CTkTextbox(Tabs.tab(tab), width=30)
    EntryAddress.grid(row=7, column=2, padx=5, pady=5, columnspan=2, sticky="news")

    EnterButton = c.CTkButton(Tabs.tab(tab), text="Enter")
    EnterButton.grid(row=8, column=2, padx=5, pady=30, columnspan=2, sticky="news")


def SelectUpdateValue(choice):
    global DynamicUpdateLabel
    global DynamicUpdateWidget

    DynamicUpdateLabel.configure(text=choice)
    DynamicUpdateWidget.destroy()

    if choice in ["Name", "Class", "Date Of Birth", "Gender", "Phone Number", "Guardian's Name"]:
        DynamicUpdateWidget = c.CTkEntry(Tabs.tab("Update Student Data"), placeholder_text="Enter "+choice, width=150)
        DynamicUpdateWidget.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Address":
        DynamicUpdateWidget = c.CTkTextbox(Tabs.tab("Update Student Data"), width=30)
        DynamicUpdateWidget.grid(row=2, column=1, sticky="news", padx=5, pady=5, columnspan=2)

def SelectTableMainFrame(choice):
    global Tabs
    Tabs.destroy()

    if choice == "Student Table":
        Tabs = c.CTkTabview(window, corner_radius=20, width=400)

        Tabs.add("Insert Student Data")
        Tabs.add("Update Student Data")
        Tabs.add("Delete Student Data")

        Tabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

        create_insert_window_widgets("Insert Student Data")
        createUpdateWindowWidgets("Update Student Data")
        createDeleteWindowWidgets("Delete Student Data")

    elif choice=="Result Table":

        Tabs = c.CTkTabview(window, corner_radius=20, width=400)

        Tabs.add("Insert Student Result Data")
        Tabs.add("Update Student Result Data")
        Tabs.add("Delete Student Result Data")

        Tabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

        RollNo = c.CTkLabel(Tabs.tab("Insert Student Result Data"), text="RollNo")  # primary key
        RollNo.grid(row=0, column=0)

        Name = c.CTkLabel(Tabs.tab("Insert Student Result Data"), text="Name")
        Name.grid(row=1, column=0)

        Class = c.CTkLabel(Tabs.tab("Insert Student Result Data"), text="Class")
        Class.grid(row=2, column=0)

        EntryRollNumber = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="Enter Roll Number")
        EntryRollNumber.grid(row=0, column=1, padx=5, pady=5)

        EntryFirstName = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="First Name")
        EntryFirstName.grid(row=1, column=1, padx=5, pady=5)
        EntrySecondName = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="Last Name")
        EntrySecondName.grid(row=1, column=2, padx=5, pady=5)

        EntryClass = c.CTkEntry(Tabs.tab("Insert Student Result Data"), placeholder_text="Enter Class")
        EntryClass.grid(row=2, column=1, padx=5, pady=5)

        EnterButton = c.CTkButton(Tabs.tab("Insert Student Result Data"), text="Enter")
        EnterButton.grid(row=8, column=2, padx=5, pady=30, columnspan=2, sticky="news")


window = c.CTk()
window.geometry("1280x720")

window.title("School Management System")
window.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, uniform="uniform columns")

window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="uniform rows")
# Side Frame
sidebar = c.CTkFrame(window, corner_radius=20, width=120)

sidebar.grid(column=0, row=0, rowspan=7, sticky="news", padx=10, pady=10)
sideFrameSelectTable = c.CTkOptionMenu(sidebar, values=["Student Table", "Result Table"], command=SelectTableMainFrame)

sideFrameSelectTable.grid(row=1, column=0, sticky="wen", padx=10, pady=10)

sidebar.bind('<Button-1>', removeFocusSidebar)
Title = c.CTkLabel(sidebar, text="SMS", height=10, width=20, font=c.CTkFont(size=30, weight="bold"))

# Side Frame

# Search Frame

Title.grid(row=0, column=0, sticky="ew", padx=40, pady=40)
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

Tabs = c.CTkTabview(window, corner_radius=20, width=400)
Tabs.add("Insert Student Data")
Tabs.add("Update Student Data")
Tabs.add("Delete Student Data")

Tabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

create_insert_window_widgets("Insert Student Data")
createUpdateWindowWidgets("Update Student Data")
createDeleteWindowWidgets("Delete Student Data")


window.mainloop()
