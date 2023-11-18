import tkinter as tk
import customtkinter  # Assuming you have a module or class named 'customtkinter' with CTkProgressBar

class YourApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Your Tkinter App")

        # Create the frame for the progress bar
        self.slider_progressbar_frame = tk.Frame(self.master)
        self.slider_progressbar_frame.pack(padx=20, pady=20)

        # Create and place the custom progress bar widget
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")

if __name__ == "__main__":
    root = tk.Tk()
    app = YourApp(root)
    root.mainloop()