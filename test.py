import customtkinter as c

def switch_to_frame1():
    global frame_right
    frame_right.destroy()

    frame_right = c.CTkFrame(window)
    frame_right.grid(row=0, column=1, sticky="news", padx=10, pady=10)

    label = c.CTkLabel(frame_right, text="frame asfg 111111")
    label.pack()

def switch_to_frame2():
    global frame_right
    frame_right.destroy()

    frame_right = c.CTkFrame(window)
    frame_right.grid(row=0, column=1, sticky="news", padx=10, pady=10)

    label = c.CTkLabel(frame_right, text="frame 22222")
    label.pack()


window = c.CTk()
window.geometry("720x480")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=7)

frame_left = c.CTkFrame(window)
frame_left.grid(row=0, column=0, sticky="news", padx=10, pady=10)

button = c.CTkButton(frame_left, text="frame one 11", fg_color="#505050", command=switch_to_frame1)
button.grid(row=0, column=0, padx=10, pady=10, sticky="news")

button2 = c.CTkButton(frame_left, text="frame two 22", fg_color="#505050", command=switch_to_frame2)
button2.grid(row=1, column=0, padx=10, pady=10)

# djskfvhgsldfkjghsdf

frame_right = c.CTkFrame(window)
frame_right.grid(row=0, column=1, sticky="news", padx=10, pady=10)

label = c.CTkLabel(frame_right, text="frame asfg 111111")
label.pack()

window.mainloop()
