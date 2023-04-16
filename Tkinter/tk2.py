from tkinter import *
root = Tk()

# with x hight
root.geometry("733x337")

# with, hight
root.minsize(200,100)
root.maxsize(733,337)
csl=Label(text="This is basic calculator")
csl.pack()


root.mainloop()
