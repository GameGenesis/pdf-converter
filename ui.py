import os
import time
from tkinter import StringVar, TOP, filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageGrab
import customtkinter

class Tk(customtkinter.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)



app = Tk()
app.title("Live Laugh Love PDF Converter")
app.geometry("800x600")

filePaths = []

def displayImages():
    index = 0
    max_height = 130
    for path in filePaths:
        pil_image = Image.open(os.path.join(path))
        width, height = pil_image.size
        aspect_ratio = max_height / height
        image = customtkinter.CTkImage(light_image=pil_image, size=(width*aspect_ratio, height*aspect_ratio))
        label = customtkinter.CTkLabel(master=frame, image=image, text='')
        label.grid(column=index, row=0, padx=5, pady=10)
        index += 1

def openfile():
    filePaths.extend(list(filedialog.askopenfilenames(initialdir = "/",title = "Select file",
                        filetypes = (("PNG Files","*.png"),("JPG Files","*.jpg"),("JPEG Files","*.jpeg"),("All Files","*.*")))))
    pathLabel.configure(text=filePaths)
    displayImages()

def get_clipboard_image(event):
    try:
        img = ImageGrab.grabclipboard()
        img.save(f"images/clipboard{time.strftime('%Y%m%d%H%M%S')}.jpg")
        filePaths.append("images/clipboard.jpg")
        displayImages()
    except:
        print("No image on the clipboard")

def get_path(event):
    pathLabel.configure(text=event.data)

custom_font =("Arial",30,'bold')
button = customtkinter.CTkButton(app, text="➕ \n\nDrag & Drop or Click Here", corner_radius=10,
                                height=250, font=custom_font, command=openfile)
button.pack(expand=False, fill="both", padx=100, pady=30)

nameVar = StringVar()

pathLabel = customtkinter.CTkLabel(app, text="Drag and drop file in the entry box")
pathLabel.pack(side=TOP)

button.drop_target_register(DND_FILES)
button.dnd_bind("<<Drop>>", get_path)

frame = customtkinter.CTkScrollableFrame(master=app, height=150, corner_radius=10, orientation="horizontal")
frame.pack(padx=100, pady=20, fill="both")

app.bind('<Control-v>', get_clipboard_image)

app.mainloop()