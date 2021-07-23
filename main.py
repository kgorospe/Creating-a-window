
from tkinter import *

def create_window():
    new_window = Tk()
    window.destroy()
    new_window.title('Welcome to my second window')
    label = Label(new_window, text="Hello World").pack()

window = Tk()
window.title('My First Window')
Button(window, text="Next Window", command=create_window).pack()
window.mainloop()
