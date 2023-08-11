import customtkinter as c
import tkinter as tk

c.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

window = c.CTk()
window.geometry("1280x720")
window.title("School Management System")

window.columnconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
# window.rowconfigure(1, weight=9)

sidebar = c.CTkFrame(window, corner_radius=20, width=120)
sidebar.grid(column=0, row=0, rowspan=10, sticky="news", padx=10, pady=10)

Title = c.CTkLabel(sidebar, text="SMS", height=10, width=20, font=c.CTkFont(size=30, weight="bold"))
Title.grid(row=0, column=0, sticky="ew", padx=40, pady=40)

tabs = c.CTkTabview(window, corner_radius=20)

tabs.add("Insert Student Data")
tabs.add("Update Student Data")
tabs.add("Delete Student Data")
tabs.add("Search Student Data")

RollNo = c.CTkLabel(tabs.tab("Insert Student Data"), text="RollNo")  # primary key
Name = c.CTkLabel(tabs.tab("Insert Student Data"), text="Name")
Class = c.CTkLabel(tabs.tab("Insert Student Data"), text="Class")
DateOfBirth = c.CTkLabel(tabs.tab("Insert Student Data"), text="DateOfBirth")
Gender = c.CTkLabel(tabs.tab("Insert Student Data"), text="Gender")
PhoneNumber = c.CTkLabel(tabs.tab("Insert Student Data"), text="Phone")
GuardianName = c.CTkLabel(tabs.tab("Insert Student Data"), text="GuardianName")
Address = c.CTkLabel(tabs.tab("Insert Student Data"), text="Address")

RollNo.grid(row=1, column=1)
Name.grid(row=2, column=1)
Class.grid(row=3, column=1)
DateOfBirth.grid(row=4, column=1)
Gender.grid(row=5, column=1)
PhoneNumber.grid(row=6, column=1)
GuardianName.grid(row=7, column=1)
Address.grid(row=8, column=1)

EntryRollNumber = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Enter Roll Number")

EntryFirstName = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="First Name")
EntrySecondName = c.CTkEntry(tabs.tab("Insert Student Data"), placeholder_text="Second Name")

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

EntryRollNumber.grid(row=1, column=2, padx=5, pady=5)

EntryFirstName.grid(row=2, column=2, padx=5, pady=5)
EntrySecondName.grid(row=2, column=3, padx=5, pady=5)

EntryClass.grid(row=3, column=2, padx=5, pady=5)

EntryDay.grid(row=4, column=2, padx=5, pady=5)
EntryMonth.grid(row=4, column=3, padx=5, pady=5)
EntryYear.grid(row=4, column=4, padx=5, pady=5)

EntryMaleGender.grid(row=5, column=2, padx=5, pady=5)
EntryFemaleGender.grid(row=5, column=3, padx=5, pady=5)

EntryPhoneNumber.grid(row=6, column=2, padx=5, pady=5, columnspan=2, sticky="ew")
EntryGuardianName.grid(row=7, column=2, padx=5, pady=5, columnspan=2, sticky="ew")
EntryAddress.grid(row=8, column=2, padx=5, pady=5, columnspan=2, sticky="news")

tabs.grid(row=0, column=1, columnspan=4, rowspan=7, sticky="news", padx=10, pady=10)

SearchBar = c.CTkEntry(window, placeholder_text="Search")
SearchBar.grid(row=0, column= 5, sticky="ew")


window.mainloop()
