# Import necessary modules
import customtkinter as c
from Center_window import center_window
from Backend.backend import get_student_data  # Import your backend function here


c.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"

def create_student_panel(roll_number, username):
    root = c.CTk()
    root.title("Student Panel")
    root.resizable(False, False)

    # Function to display student information
    def display_student_info():
        student_data = get_student_data(roll_number)

        if student_data:
            # Clear previous data
            for widget in labels_frame.winfo_children():
                widget.destroy()

            for widget in values_frame.winfo_children():
                widget.destroy()

            # Display student information in the frames
            labels = ["Roll Number", "Name", "Class", "Date Of Birth", "Gender", "Phone Number",
                      "Guardian Name", "Address"]
            for index, label_text in enumerate(labels):
                label = c.CTkLabel(labels_frame, text=label_text)
                label.grid(row=index, column=0, sticky="w", padx=10, pady=(10, 0))

                value = c.CTkLabel(values_frame, text=str(student_data[index]))
                value.grid(row=index, column=1, sticky="w", padx=10, pady=(10, 0))

        else:
            # Display a message if no data is found for the provided roll number
            message_label = c.CTkLabel(labels_frame, text="No data found for the given roll number.")
            message_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

    # Create UI elements
    username_label = c.CTkLabel(root, text=f"Username: {username}")
    username_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(20, 0))

    labels_frame = c.CTkFrame(root)
    labels_frame.grid(row=1, column=0, sticky="w", padx=10, pady=(10, 10))

    values_frame = c.CTkFrame(root)
    values_frame.grid(row=1, column=1, sticky="w", padx=10, pady=(10, 10))

    roll_number_label = c.CTkLabel(labels_frame, text="Roll Number:")
    roll_number_label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

    roll_number_value = c.CTkLabel(values_frame, text=str(roll_number))
    roll_number_value.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 0))

    # Call the function to display student information
    display_student_info()

    center_window(root)
    root.mainloop()

