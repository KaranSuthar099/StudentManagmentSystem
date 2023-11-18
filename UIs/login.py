import tkinter as tk
import customtkinter as c
from CTkMessagebox import CTkMessagebox

def change_widgets():
    global user_var

    # to delete the current widgets
    for widget in widget_frame.winfo_children():
        widget.grid_remove()

    if user_var.get() == 0:
        roll_no_entry.grid(row=1, column=1, padx=10, pady=10)
        roll_no_label.grid(row=1, column=0, padx=15, pady=10)
        username_entry.grid(row=0, column=1, padx=10, pady=10)
        username_label.grid(row=0, column=0, padx=15, pady=10)
    else:
        password_entry.grid(row=2, column=1, padx=10, pady=10)
        password_label.grid(row=2, column=0, padx=15, pady=10)
        admin_id_entry.grid(row=1, column=1, padx=10, pady=10)
        admin_id_label.grid(row=1, column=0, padx=15, pady=10)

        # Call update_idletasks to force an immediate update
    login.update_idletasks()


def authenticate():
    if user_var.get() == 0:
        pass
    elif user_var.get() == 1:
        if admin_id_entry.get() == "admin" and password_entry.get() == "root":
            CTkMessagebox(title="Login Success!!", message="You have been successfully logged-In",
                          icon="check", option_1="OK")
        else:
            CTkMessagebox(title="Login Error",
                          message="Oops! Incorrect login details. Please check and try again",
                          icon="cancel", option_1="Retry")
    else:
        CTkMessagebox(title="Login Error",
                      message="Oops! Something went wrong ",
                      icon="cancel", option_1="Retry")


login = c.CTk()
login.resizable(False, False)

# Subtitle
title = c.CTkLabel(login, width=200, text="Login", font=("roboto", 36))
title.grid(row=0, column=0, padx=250, pady=[50, 10])

user_var = tk.IntVar(value=1)
student = c.CTkRadioButton(login, text="Student", variable=user_var, value=0, command=change_widgets)
student.grid(row=1, column=0, padx=250, pady=10)
admin = c.CTkRadioButton(login, text="Admin", variable=user_var, value=1, command=change_widgets)
admin.grid(row=2, column=0, padx=250, pady=10)

# Frame
widget_frame = c.CTkFrame(login, corner_radius=10)
widget_frame.grid(row=3, column=0, columnspan=2, padx=250, pady=10)

# login as a student
username_label = c.CTkLabel(widget_frame, text="Username:")
username_entry = c.CTkEntry(widget_frame, corner_radius=10)
roll_no_label = c.CTkLabel(widget_frame, text="Roll No:")
roll_no_entry = c.CTkEntry(widget_frame, corner_radius=10)

#login as Admin
admin_id_label = c.CTkLabel(widget_frame, text="Admin id:")
admin_id_entry = c.CTkEntry(widget_frame, corner_radius=10)
password_label = c.CTkLabel(widget_frame, text="Password:")
password_entry = c.CTkEntry(widget_frame, show="*", corner_radius=10)

# Login Button
login_button = c.CTkButton(login, text="Login", width=250, fg_color="#138808",
                           hover_color="#0E6606", corner_radius=50,  command=authenticate)
login_button.grid(row=4, column=0, padx=250, pady=[10, 50], sticky="ew")

change_widgets()

login.mainloop()
