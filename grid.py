from tkinter import *

# In kinter everything is a widget
# first thing I create will be the root widget
root = Tk() #  must go first

# 1st step process
#creating a LAbel widget
myLabel1 = Label(root, text="Hello Joshua!")
myLabel2 = Label(root, text="I am FararaTheArtist")

# shoving it onto the screen
# mylabel1.pack()

# 2nd step process
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


root.mainloop()

