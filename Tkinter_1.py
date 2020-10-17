from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="cyan")
button2 = Button(topFrame, text="Button 2", fg="red")
button3 = Button(topFrame, text="Button 3", fg="purple")
button4 = Button(bottomFrame, text="Button 4", fg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

root.mainloop()

