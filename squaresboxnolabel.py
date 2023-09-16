from tkinter import*
from tkinter import ttk
from tkinter import filedialog
import customtkinter


def button_callback():
    print("open file explorer lul")

app = customtkinter.CTk()
app.title("Live Laugh Love PDF Converter")
app.geometry("800x500")

def openfile():
    return filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))

<<<<<<< Updated upstream
buttonPNG = customtkinter.CTkButton(app, width=120, height=50, text="Add PNG files", command=openfile)
buttonPNG.pack(padx=20, pady=80)
=======
buttonPNG = customtkinter.CTkButton(app, width=120, height=50, text="Add PNG/JPG files", command=openfile)
buttonPNG.pack(padx=20, pady=20)

nameVar = StringVar()

pathLabel = customtkinter.CTkLabel(app, text="Drag and drop file in the entry box")
pathLabel.pack(side=TOP)

buttonPNG.drop_target_register(DND_ALL)
buttonPNG.dnd_bind("<<Drop>>", get_path)
>>>>>>> Stashed changes

app.mainloop()