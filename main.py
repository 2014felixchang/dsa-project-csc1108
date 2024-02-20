from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("700x400")

set_appearance_mode("dark")

btn = CTkButton(
    master=app, 
    text="Click me", 
    corner_radius=32, 
    fg_color="#C850C0", 
    hover_color="#4158D0", 
    border_color="#FFD700",
    border_width=2,
    command=lambda: print("Hello World")
)

btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()