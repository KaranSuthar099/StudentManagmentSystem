import customtkinter as c

c.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

window = c.CTk()
window.geometry("1280x720")
window.title("School Management System")

window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight=1)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight=1)
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
Name = c.CTkLabel(tabs.tab("Insert Student Data"),text="Name")
Class = c.CTkLabel(tabs.tab("Insert Student Data"), text="Class")
DateOfBirth = c.CTkLabel(tabs.tab("Insert Student Data"), text="DateOfBirth")
Gender = c.CTkLabel(tabs.tab("Insert Student Data"), text="Gender")
Phone = c.CTkLabel(tabs.tab("Insert Student Data"), text="Phone")
GurdianName = c.CTkLabel(tabs.tab("Insert Student Data"), text="GurdianName")
Address = c.CTkLabel(tabs.tab("Insert Student Data"), text="Address")

RollNo.grid(row=2, column=1)
Name.grid(row=3, column=1)
Class.grid(row=4, column=1)
DateOfBirth.grid(row=5, column=1)
Gender.grid(row=6, column=1)
Phone.grid(row=7, column=1)
GurdianName.grid(row=8, column=1)
Address.grid(row=9, column=1)


tabs.grid(row=0, column=1, sticky="news", rowspan=10, columnspan=9, padx=10, pady=10)

window.mainloop()
