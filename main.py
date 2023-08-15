import tkinter as tk

import customtkinter as c

c.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

flagFirstRun = 0
value_check = 0


def SelectUpdateValue(choice):
    UpdateName.configure(text="Enter " + choice)
    global DynamicWidget
    DynamicWidget.destroy()

    if choice == "Name":
        DynamicWidget = c.CTkEntry(tabs.tab("Update Student Data"), placeholder_text="Enter Namrtyerhte")
        DynamicWidget.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Class":
        DynamicWidget = c.CTkEntry(tabs.tab("Update Student Data"), placeholder_text="Enter Namertherhrthe")
        DynamicWidget.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Date Of Birth":
        UpdateName.configure(text="Enter " + choice)
        DynamicWidget = c.CTkEntry(tabs.tab("Update Student Data"), width=200,
                                   placeholder_text="in format (YYYY/MM/DD)")
        DynamicWidget.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Gender":
        DynamicWidget = c.CTkOptionMenu(tabs.tab("Update Student Data"), values=["Male", "Female"])
        DynamicWidget.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Phone Number":
        DynamicWidget = c.CTkEntry(tabs.tab("Update Student Data"), placeholder_text="Enter Phone Number")
        DynamicWidget.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Guardian's Name":
        DynamicWidget = c.CTkEntry(tabs.tab("Update Student Data"), placeholder_text="Enter Guardian's Name")
        DynamicWidget.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    elif choice == "Address":
        DynamicWidget = c.CTkTextbox(tabs.tab("Update Student Data"), width=30)
        DynamicWidget.grid(row=1, column=1, sticky="news", padx=5, pady=5, columnspan=2)


window = c.CTk()
window.geometry("1280x720")
window.title("School Management System")

window.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="uniform columns")
window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="uniform rows")
# window.rowconfigure(1, weight=9)

sidebar = c.CTkFrame(window, corner_radius=20, width=120)
sidebar.grid(column=0, row=0, rowspan=7, sticky="news", padx=10, pady=10)

Title = c.CTkLabel(sidebar, text="SMS", height=10, width=20, font=c.CTkFont(size=30, weight="bold"))
Title.grid(row=0, column=0, sticky="ew", padx=40, pady=40)

tabs = c.CTkTabview(window, corner_radius=20, width=400)

tabs.add("Insert Student Data")
tabs.add("Update Student Data")
tabs.add("Delete Student Data")

RollNo = c.CTkLabel(tabs.tab("Insert Student Data"), text="RollNo")  # primary key
Name = c.CTkLabel(tabs.tab("Insert Student Data"), text="Name")
Class = c.CTkLabel(tabs.tab("Insert Student Data"), text="Class")
DateOfBirth = c.CTkLabel(tabs.tab("Insert Student Data"), text="DateOfBirth")
Gender = c.CTkLabel(tabs.tab("Insert Student Data"), text="Gender")
PhoneNumber = c.CTkLabel(tabs.tab("Insert Student Data"), text="Phone")
GuardianName = c.CTkLabel(tabs.tab("Insert Student Data"), text="GuardianName")
Address = c.CTkLabel(tabs.tab("Insert Student Data"), text="Address")

RollNo.grid(row=0, column=1)
Name.grid(row=1, column=1)
Class.grid(row=2, column=1)
DateOfBirth.grid(row=3, column=1)
Gender.grid(row=4, column=1)
PhoneNumber.grid(row=5, column=1)
GuardianName.grid(row=6, column=1)
Address.grid(row=7, column=1)

EntryRollNumber = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Enter Roll Number")

EntryFirstName = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="First Name")
EntrySecondName = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Last Name")

EntryClass = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Enter Class")

EntryDay = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Day")
EntryMonth = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Month")
EntryYear = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Year")

RadioVal = tk.IntVar(value=0)

EntryMaleGender = c.CTkRadioButton(tabs.tab("Insert Student Data"), text="Male", variable=RadioVal, value=0)
EntryFemaleGender = c.CTkRadioButton(tabs.tab("Insert Student Data"), text="Female", variable=RadioVal, value=1)

EntryPhoneNumber = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Enter Phone number")
EntryGuardianName = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Enter Guardian's Name")

EntryAddress = c.CTkTextbox(tabs.tab("Insert Student Data"), width=30)

EnterButton = c.CTkButton(tabs.tab("Insert Student Data"), text="Enter")

EntryRollNumber.grid(row=0, column=2, padx=5, pady=5)

EntryFirstName.grid(row=1, column=2, padx=5, pady=5)
EntrySecondName.grid(row=1, column=3, padx=5, pady=5)

EntryClass.grid(row=2, column=2, padx=5, pady=5)

EntryDay.grid(row=3, column=2, padx=5, pady=5)
EntryMonth.grid(row=3, column=3, padx=5, pady=5)
EntryYear.grid(row=3, column=4, padx=5, pady=5)

EntryMaleGender.grid(row=4, column=2, padx=5, pady=5)
EntryFemaleGender.grid(row=4, column=3, padx=5, pady=5)

EntryPhoneNumber.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="ew")
EntryGuardianName.grid(row=6, column=2, padx=5, pady=5, columnspan=2, sticky="ew")
EntryAddress.grid(row=7, column=2, padx=5, pady=5, columnspan=2, sticky="news")

EnterButton.grid(row=8, column=2, padx=5, pady=20, columnspan=2, sticky="news")

tabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

# making a new frame
SearchFrame = c.CTkFrame(window, corner_radius=20)

SearchFrame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="uniform")
SearchFrame.rowconfigure((0, 1, 2), weight=1, uniform="uniform")
SearchFrame.grid(row=0, column=5, rowspan=7, columnspan=3, sticky="news", padx=10, pady=10)

SearchBar = c.CTkEntry(SearchFrame, placeholder_text="S e a r c h", width=200)
SearchBar.grid(row=0, column=0, sticky="sew", padx=10, pady=10, columnspan=2)

SearchButton = c.CTkButton(SearchFrame, text="Search")
SearchButton.grid(row=0, column=2, sticky="sew", padx=[5, 5], pady=10)

SelectTable = c.CTkOptionMenu(SearchFrame, values=["Student Table", "Result Table"])
SelectTable.grid(row=1, column=0, sticky="wen", padx=10, pady=10)

# update student tab

UpdateLabel = c.CTkLabel(tabs.tab("Update Student Data"), text="You want to Update ")
UpdateLabel.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

UpdateSelect = c.CTkOptionMenu(tabs.tab("Update Student Data"), width=400, command=SelectUpdateValue
                               , values=["Name", "Class",
                                         "Date Of Birth", "Gender",
                                         "Phone Number", "Guardian's Name",
                                         "Address"])
UpdateSelect.grid(row=0, column=1, columnspan=4, sticky="ew", padx=5, pady=5)

UpdateName = c.CTkLabel(tabs.tab("Update Student Data"), text="Name")
UpdateName.grid(row=1, column=0, sticky="w", padx=5, pady=5)

DynamicWidget = c.CTkEntry(tabs.tab("Update Student Data"), placeholder_text="Enter Name")
DynamicWidget.grid(row=1, column=1, sticky="w", padx=5, pady=5)

window.mainloop()
