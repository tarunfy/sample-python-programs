from tkinter import *

root = Tk()
# Simple gui with a text:
# label1 = Label(root, text="Hello World")
# label1.pack()

# ADDING BUTTONS:
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text="Button 1", fg="cyan")
# button2 = Button(topFrame, text="Button 2", fg="red")
# button3 = Button(topFrame, text="Button 3", fg="purple")
# button4 = Button(bottomFrame, text="Button 4", fg="green")

# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack()

# ADDING WIDGETS:
# one = Label(root, text= "One", bg="red", fg="green")
# one.pack()

# two = Label(root, text= "Two", bg="blue", fg="yellow")
# two.pack(fill=X)

# three = Label(root, text= "Three", bg="green", fg="black")
# three.pack(side=LEFT, fill=Y)

# ADDING WIDGETS USING GRID:
# label1 = Label(root, text="Name")
# label2 = Label(root, text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)

# label1.grid(row=0, sticky=E)
# label2.grid(row=1, sticky=E)

# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)

# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)

# Calling a function when a button is clicked:
# Trick 1:
def printName():
    print("Hello my name is Tarun")
button_1 = Button(root, text= "Print my name", command=printName)
button_1.pack()

# Trick 2:
# def printName(event): 
#     print("Hello my name is Tarun")
# button_1 = Button(root, text= "Print my name")
# button_1.bind("<Button-1>", printName)
# button_1.pack()
root.mainloop()

