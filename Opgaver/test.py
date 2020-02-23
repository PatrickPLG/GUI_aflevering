from tkinter import *

d

root = Tk()
photo_path = "Dog.gif"

photo = PhotoImage(
    file = photo_path,
    )
label = Label(
    image = photo
    )
animate = Button(
    root,
    text = "animate",
    command = run_animation
    )

label.pack()
animate.pack()

root.mainloop()