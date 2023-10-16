from tkinter import *

# In kinter everything is a widget
# first thing I create will be the root widget
root = Tk() #  must go first

#creating a LAbel widget
myLabel = Label(root, text="Hello Joshua!")

# shoving it onto the screen
myLabel.pack()

root.mainloop()

# lets explore what we have