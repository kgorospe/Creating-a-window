
from tkinter import * #Explain what this is - JG

def create_window():
    new_window = Tk()
    window.destroy()
    new_window.title('Welcome to my second window')
    label = Label(new_window, text="Hello World").pack()

window = Tk() #Explain what this is - JG
window.title('My First Window')
print("here")
Button(window, text="Next Window", command=create_window).pack()
window.mainloop() #Explain what this is - JG
