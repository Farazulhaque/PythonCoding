# from tkinter import *

# root = Tk()
# root.geometry("200x55")


# def One():
#     print("Button one clicked")


# def Two():
#     print("Button two clicked")


# btn1 = Button(root, text="One")
# btn1.pack()
# btn2 = Button(root, text="Two")
# btn2.pack()

# btn1.bind('<Button-1>', One)
# btn2.bind('<Button-1>', Two)

# root.mainloop()

from tkinter import *

root = Tk()
root.geometry("200x55")

btn1 = Button(root, text="One")
btn1.pack()
btn2 = Button(root, text="Two")
btn2.pack()

root.mainloop()
