
from tkinter import * #we are importing tkinter into python so we can create an interface for the user

def create_window():
    new_window = Tk()
    window.destroy()
    new_window.title('Welcome to my second window')
    label = Label(new_window, text="Hello World").pack()

window = Tk() ##we created a variable named 'window' and we're setting it equal to the Window that will be created using tkinter
window.title('My First Window')
print("here") #Adding a print statement here won't make it available in the window bc it's not being applied to the window. it will show up in the console after hitting run
Button(window, text="Next Window", command=create_window).pack()
window.mainloop() #mainloop = "end"; it indicates an end to the script. python will not be able to execute the code without it
