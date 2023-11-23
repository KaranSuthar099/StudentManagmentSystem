import customtkinter
from CTkTable import *
from backend import get_all_data

root = customtkinter.CTk()

value = get_all_data()

scrollable_frame = customtkinter.CTkScrollableFrame(root, label_text="CTkScrollableFrame")
scrollable_frame.grid(row=0, column=0, columnspan=9, padx=(20, 0), pady=(20, 0), sticky="nsew")
scrollable_frame.grid_columnconfigure(0, weight=1)

table = CTkTable(scrollable_frame, row=25, column=8, values=value)
table.grid(sticky="nsew")  # Use grid instead of pack

root.mainloop()
