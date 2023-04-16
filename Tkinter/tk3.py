from tkinter import *
#for JPG formet
from PIL import Image, ImageTk

root=Tk()

root.geometry("733x377")

image=Image.open("Screenshot.png")
resize=image.resize((300,300),Image.ADAPTIVE)
photo=ImageTk.PhotoImage(resize)
lable=Label(image=photo).grid(row=0,column=0)
# photo1=PhotoImage(file="Screenshot.png")
# For JPG
image1=Image.open("sarthak.jpeg")
resize=image1.resize((300,300),Image.ADAPTIVE)
photo1=ImageTk.PhotoImage(resize)
lable1=Label(image=photo1).grid(row=0,column=1)
# lable.pack()
# lable1.pack()

root.mainloop()