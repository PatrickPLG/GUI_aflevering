import tkinter as tk
import date


class TestGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main_window = master
        self.main_window.title("Test")
        self.pack()
        self.controller_init()
        self.model_init()
        self.view_init()

    def controller_init(self):
        print_button = tk.Button(self, text="Print")
        print_button.pack(side="bottom")
        # Find en liste over hændelser i Tcl/Tk dokumentationen.
        # Ud over en række hændelser kan bestemte taster bindes.
        print_button.bind("<ButtonRelease>", self.model_next_day)
        print_button.bind("<Return>", self.model_next_day)
        print_button.bind("<space>", self.model_next_day)

    def model_init(self):
        self.myDate = date.Date(20, 5, 2020)

    def view_init(self):
        self.text_input = tk.Entry(self)
        self.text_input.insert(0, self.myDate.toString())
        self.text_input.pack(side="top")

    def model_next_day(self, event):
        # Brug metoden get til at returnere teksten for en widget.
        # Se i dokumentationen, eller tryk på Ctrl-shift-I efter navnet
        # på en widget i PyCharm.
        # print(self.text_input.get())
        self.myDate.setToNextDate()
        self.view_update()
        
    def view_update(self):
        self.text_input.delete(0, "end")
        self.text_input.insert(0, self.myDate.toString())
    

root = tk.Tk()
window = TestGUI(root)
window.mainloop()