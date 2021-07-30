from tkinter import *

from tkinter import messagebox


class WidgetDemo():
    def __init__(self):
        window = Tk()
        window.title("Widget Demo !")
        frame1 = Frame(window)
        frame1.pack()
        button1 = Button(text="Click Me", command=self.processButton)
        button1.pack()
        window.mainloop()

    def processButton(self):
        messagebox.showinfo("Message", "Welcome")

if __name__ == '__main__':
    window = WidgetDemo()