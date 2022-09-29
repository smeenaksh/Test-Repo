import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog

def yellowButton_callback():
    pass

def blueButton_callback():
    pass

def pinkButton_callback():
    pass

def orangeButton_callback():
    pass

def noneButton_callback():
    pass

def displayImage(displayImage):
    ImagetoDisplay = displayImage.resize((900,600), Image.ANTIALIAS)
    ImagetoDisplay = ImageTk.PhotoImage(ImagetoDisplay)
    showWindow.config(image=ImagetoDisplay)
    showWindow.photo_ref = ImagetoDisplay
    showWindow.pack()

def importButton_callback():
    global originalImage
    filename = filedialog.askopenfilename()
    originalImage = Image.open(filename)
    displayImage(originalImage)

def saveButton_callback():
    pass

def closeButton_callback():
    window.destroy()

def brightness_callback(brightness_pos):
    print(brightness_pos)

def contrast_callback(contrast_pos):
    print(contrast_pos)

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry(f'{screen_width}x{screen_height}')

Frame1 = tk.Frame(window, height=20, width=200)
Frame1.pack(anchor=tk.N)

Frame2 = tk.Frame(window, height=20)
Frame2.pack(anchor=tk.NW)

Frame3 = tk.Frame(window, height=20)
Frame3.pack(anchor=tk.N)

importButton = tk.Button(Frame1, text="Import", padx=10, pady=5, command=importButton_callback)
importButton.grid(row=0, column=0)

saveButton = tk.Button(Frame1, text="save", padx=10, pady=5, command=saveButton_callback)
saveButton.grid(row=0, column=1)

closeButton = tk.Button(Frame1, text="close", padx=10, pady=5, command=closeButton_callback)
closeButton.grid(row=0, column=2)

brightnessSlider = tk.Scale(Frame2, label="brightness", from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
                            resolution=0.1, command=brightness_callback)
brightnessSlider.pack(anchor=tk.N)

contrastSlider = tk.Scale(Frame2, label="contrast", from_=0, to=2, orient=tk.HORIZONTAL, length=screen_width,
                             command=contrast_callback)
contrastSlider.pack(anchor=tk.N)

YellowButton = tk.Radiobutton(Frame3, text="Yellow", width=20, value=1, command=yellowButton_callback)
YellowButton.grid(row=0, column=0)

blueButton = tk.Radiobutton(Frame3, text="Blue", width=20, value=2, command=blueButton_callback)
blueButton.grid(row=0, column=1)

pinkButton = tk.Radiobutton(Frame3, text="Pink", width=20, value=3, command=pinkButton_callback)
pinkButton.grid(row=0, column=2)

orangeButton = tk.Radiobutton(Frame3, text="Orange", width=20, value=4, command=orangeButton_callback)
orangeButton.grid(row=0, column=3)

noneButton = tk.Radiobutton(Frame3, text="None", width=20, value=5, command=noneButton_callback)
noneButton.grid(row=0, column=4)
noneButton.select()

showWindow = tk.Label(window)
showWindow.pack()
tk.mainloop()