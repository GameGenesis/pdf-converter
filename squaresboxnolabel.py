from tkinter import StringVar, TOP, filedialog, ttk
from tkinterdnd2 import TkinterDnD, DND_ALL
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
    filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",
                        filetypes = (("PNG Files","*.png"),("JPG Files","*.jpg"),("JPEG Files","*.jpeg"),("All Files","*.*")))
    pathLabel.configure(text=filePath)

def get_path(event):
    pathLabel.configure(text=event.data)

buttonPNG = customtkinter.CTkButton(app, width=120, height=50, text="Add PNG files", command=openfile)
buttonPNG.pack(padx=20, pady=20)

nameVar = StringVar()

pathLabel = customtkinter.CTkLabel(app, text="Drag and drop file in the entry box")
pathLabel.pack(side=TOP)

buttonPNG.drop_target_register(DND_ALL)
buttonPNG.dnd_bind("<<Drop>>", get_path)

app.mainloop()