import customtkinter as c
from Center_window import center_window

c.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


def show_splash_screen():
    splash_root = c.CTk()
    splash_root.resizable(False, False)
    splash_root.title("Student Management System")

    frame = c.CTkFrame(splash_root, corner_radius=15)
    frame.grid(row=0, column=0, padx=75, pady=30)

    title = c.CTkLabel(frame, text="Loading", font=(("roboto", 26)))
    title.grid(row=0, column=0, padx=75, pady=10)

    # Create and place the custom progress bar widget
    progressbar_1 = c.CTkProgressBar(frame, progress_color="#ffffff")
    progressbar_1.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="ew")
    progressbar_1.configure(mode="indeterminate")
    progressbar_1.start()

    # to kill the activity after 3 seconds
    splash_root.after(2000, lambda: splash_root.destroy())  # Use lambda to delay the execution

    # Centering the window
    center_window(splash_root)

    # Start the Tkinter event loop for the splash screen
    splash_root.mainloop()
