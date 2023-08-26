import customtkinter
from tkinter import ttk
from ttkthemes import ThemedStyle


main = customtkinter.CTk()


seg_button_1 = customtkinter.CTkSegmentedButton(main, values=["CTkSegmentedButton", "Value 2", "Value 3"])
seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
seg_button_1.set("Value 2")

main.mainloop()
