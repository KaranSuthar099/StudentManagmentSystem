import tkinter as tk
import customtkinter as c
from Splash_Screen import show_splash_screen
from Center_window import center_window
from Backend.backend import *
from Admin_panel import create_admin_window
from Student_panel import create_student_panel

c.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def change_widgets():
    global user_login_choice

    # to delete the current widgets
    for widget in widget_frame.winfo_children():
        widget.grid_remove()

    if user_login_choice.get() == 0:
        username_entry.grid(row=0, column=1, padx=10, pady=[20, 5])
        username_label.grid(row=0, column=0, padx=15, pady=[20, 5])
        roll_no_entry.grid(row=1, column=1, padx=10, pady=[5, 20])
        roll_no_label.grid(row=1, column=0, padx=15, pady=[5, 20])
    else:
        admin_id_entry.grid(row=1, column=1, padx=10, pady=[20, 5])
        admin_id_label.grid(row=1, column=0, padx=15, pady=[20, 5])
        password_entry.grid(row=2, column=1, padx=10, pady=[5, 20])
        password_label.grid(row=2, column=0, padx=15, pady=[5, 20])

        # Call update_idletasks to force an immediate update
    login.update_idletasks()


def authenticate():
    if user_login_choice.get() == 0:  # login as a student
        roll = roll_no_entry.get()
        username = username_entry.get()
        data = get_student_data(roll)

        # data can be either () or the student data
        if data == ():  # if data is ()
            print("No data found with the corresponding roll number")
            CTkMessagebox(title="Error", message="No data found for the Roll Number.", icon="cancel")
        else:
            login.destroy()
            create_student_panel(roll, username)



    elif user_login_choice.get() == 1:  # login as admin
        if admin_id_entry.get() == "admin" and password_entry.get() == "root":  # if the id and pass are correct
            login.destroy()
            create_admin_window()
        else:  # if the password and id is false
            CTkMessagebox(title="Login Error",
                          message="Oops! Incorrect login details. Please check and try again",
                          icon="cancel", option_1="Retry")
    else:  # don't know how this condition will be archived but still what if :)
        CTkMessagebox(title="Login Error",
                      message="Oops! Something went wrong ",
                      icon="cancel", option_1="Retry")


show_splash_screen()

login = c.CTk()
login.resizable(False, False)

title = c.CTkLabel(login, width=200, text="Login", font=("roboto", 36))
title.grid(row=0, column=0, padx=200, pady=[20, 10])

login_frame = c.CTkFrame(login, corner_radius=20)
login_frame.grid(row=1, column=0, padx=200, pady=[5, 20])

user_login_choice = tk.IntVar(value=1)
student = c.CTkRadioButton(login_frame, text="Student", variable=user_login_choice, value=0, command=change_widgets)
student.grid(row=1, column=0, padx=10, pady=[20, 10])
admin = c.CTkRadioButton(login_frame, text="Admin", variable=user_login_choice, value=1, command=change_widgets)
admin.grid(row=2, column=0, padx=10, pady=10)

# Frame
widget_frame = c.CTkFrame(login_frame, corner_radius=10)
widget_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# login as a student
username_label = c.CTkLabel(widget_frame, text="  Username :")
username_entry = c.CTkEntry(widget_frame, corner_radius=10)
roll_no_label = c.CTkLabel(widget_frame, text="Roll Number:")
roll_no_entry = c.CTkEntry(widget_frame, corner_radius=10)

# login as Admin
admin_id_label = c.CTkLabel(widget_frame, text="  Admin id  :")
admin_id_entry = c.CTkEntry(widget_frame, corner_radius=10)
password_label = c.CTkLabel(widget_frame, text="  Password  :")
password_entry = c.CTkEntry(widget_frame, show="*", corner_radius=10)

# Login Button
login_button = c.CTkButton(login_frame, text="Login", width=250, fg_color="#138808",
                           hover_color="#0E6606", corner_radius=50, command=authenticate)
login_button.grid(row=4, column=0, padx=10, pady=[50, 10], sticky="ew")

change_widgets()
center_window(login)

login.mainloop()
