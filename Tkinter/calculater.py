from tkinter import *


root = Tk()
root.geometry("477x377")
root.title("Calculater")

scvalue= StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="lucida 27 bold")
screen.pack(fill="x",ipadx=7,padx=10)

#button

f=Frame(root,bg="gray",padx=3,pady=3)
b=Button(f,text="Log",height=1,width=3,padx=0,pady=0,font="lucida 23 bold")
b.pack(side=LEFT)

b = Button(f, text="C", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
b.pack(side=LEFT)

b = Button(f, text="<--", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
b.pack(side=LEFT)

b = Button(f, text="/", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
b.pack(side=LEFT)
f.pack()

for i in range(1,10,3):
    f=Frame(root,bg="gray",padx=3,pady=3)
    for j in range(3):
        b=Button(f,text=str(j+i),height=1,width=3,padx=0,pady=0,font="lucida 23 bold")
        b.pack(side=LEFT)

    if i==1:
        b = Button(f, text="*", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
        b.pack(side=LEFT)
    if i==4:
        b = Button(f, text="-", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
        b.pack(side=LEFT)
    if i==7:
        b = Button(f, text="+", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
        b.pack(side=LEFT)
    f.pack()


# for 0
f=Frame(root,bg="gray",padx=3,pady=3)
b=Button(f,text="0",height=1,width=3,padx=0,pady=0,font="lucida 23 bold")
b.pack(side=LEFT)

b = Button(f, text="00", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
b.pack(side=LEFT)

b = Button(f, text=".", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
b.pack(side=LEFT)

b = Button(f, text="=", height=1, width=3, padx=0, pady=0, font="lucida 23 bold")
b.pack(side=LEFT)
f.pack()
root.mainloop()