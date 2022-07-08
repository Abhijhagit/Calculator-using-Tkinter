from cProfile import label
from importlib.metadata import entry_points
from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km converter ")
window.minsize(width=500, height=500)

def something():
    t1=int(entry1.get())
    float1=t1*1.6
    label.config(text=float1)

# Labels
label = Label(text="This is new text")
label.config(text="Result" ,font=("Arial", 25))
label.place(x=330,y=10)

# buttons
new_button=Button(text="click me just",command=something)
new_button.place(x=200,y=13)

# entrys
entry1=Entry(width=20)
entry1.place(x=20,y=20)


window.mainloop()
