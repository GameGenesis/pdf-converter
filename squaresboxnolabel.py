from tkinter import StringVar, TOP, filedialog, ttk
from tkinterdnd2 import TkinterDnD, DND_ALL, DND_FILES
import customtkinter

class Tk(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

def button_callback():
    print("open file explorer lul")

app = Tk()
app.title("Live Laugh Love PDF Converter")
app.geometry("800x500")

def openfile():
    filePaths = list(filedialog.askopenfilenames(initialdir = "/",title = "Select file",
                        filetypes = (("PNG Files","*.png"),("JPG Files","*.jpg"),("JPEG Files","*.jpeg"),("All Files","*.*"))))
    pathLabel.configure(text=filePaths)

def get_path(event):
    pathLabel.configure(text=event.data)

custom_font =("Arial",30,'bold')
button = customtkinter.CTkButton(app, text="➕ \n\nDrag & Drop or Click Here", corner_radius=10,
                                 fg_color="grey", height=250, font=custom_font, command=openfile)
button.pack(expand=False, fill="both", padx=100, pady=30)

nameVar = StringVar()

pathLabel = customtkinter.CTkLabel(app, text="Drag and drop file in the entry box")
pathLabel.pack(side=TOP)

button.drop_target_register(DND_FILES)
button.dnd_bind("<<Drop>>", get_path)

app.mainloop()