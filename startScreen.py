# Importing Libraries
from tkinter import CENTER, TOP, Label, PhotoImage
import customtkinter
from PIL import Image, ImageTk 

# Themes
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Window
root = customtkinter.CTk()
root.title("PDF-POOF! Converter")

# Title
Label(root, text = "PDF-POOF! Converter", font=('Roboto', 60)).pack(side=TOP, pady = 10)

# Image
image = PhotoImage(file = "Button_Image3.png")






# Window dimensions 
root.geometry('800x600')
frame = customtkinter.CTkFrame(master=root, width=600, height=600)
# button imp to pdf
iToPButton = customtkinter.CTkButton(master=root,
                                     image = image,
                                     width = 300, 
                                     height =300,
                                     text=("IMG/JPG -> PDF"),
                                     font=('Roboto',30),
                                     compound=TOP                
                                        )

# button placement
iToPButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)

# run app
root.mainloop()

