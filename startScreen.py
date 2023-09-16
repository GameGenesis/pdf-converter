# Importing Libraries
from tkinter import*
import customtkinter


# Themes
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Window
root = customtkinter.CTk()

Label(root, text = "Converter", font=('Roboto', 60)).pack(side=TOP, pady = 10)



# Window dimensions 
root.geometry('800x600')

# button imp to pdf
iToPButton = customtkinter.CTkButton(master=root, 
                                         width = 300, 
                                         height =300, 
                                         text = 'IMG TO PDF',
                                         anchor="center"
                                        )





# button placement
iToPButton.place(relx=0.08, rely=0.25)

# run app
root.mainloop()

