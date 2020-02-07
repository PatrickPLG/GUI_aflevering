
import tkinter as tk
import date
import pet

class TestGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main_window = master
        self.main_window.title("Pet")
        self.pack()
        self.place()
        self.controller_init()
        self.model_init()
        self.view_init()
        self.name = "Allo"

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
        self.myPet = pet.Pet(0, 0, 0)

    def view_init(self):
        dateLabel = tk.Label(self, text="Current Date")
        dateLabel.config(font=("Comic Sans MS", 44))
        dateLabel.pack(side="top")
        self.text_input = tk.Entry(self)
        self.text_input.insert(0, self.myDate.toString())
        self.text_input.pack(side="top")

        energyLabel = tk.Label(self, text="Energy")
        energyLabel.config(font=("Comic Sans MS", 44))
        energyLabel.pack(side="left")
        self.text_energy = tk.Entry(self)
        self.text_energy.insert(0, self.myPet.energy)+
        self.text_energy.pack(side="bottom")

        self.text_hunger = tk.Entry(self)
        self.text_hunger.insert(0, self.myPet.hunger)
        self.text_hunger.pack(side="bottom")
        
    def model_next_day(self, event):
        # Brug metoden get til at returnere teksten for en widget.
        # Se i dokumentationen, eller tryk på Ctrl-shift-I efter navnet
        # på en widget i PyCharm.
        # print(self.text_input.get())
        self.myDate.setToNextDate()
        self.myPet.setToNextHour()

        # Death checks
        if (self.myPet.deathHungerOver() == True):
            print(self.name + " døde på grund af mangel på mad...")
        if (self.myPet.deathEnergyOver() == True):
            print(self.name + " døde på grund af den ikke fik nok motion.")
        if (self.myPet.deathEnergyUnder() == True):
            print(self.name + " døde på grund af du gav det for meget mad")
        if (self.myPet.deathHungerUnder() == True):
            print(self.name + " døde på grund af for meget motion")
        # ------------

        self.view_update()
        #print(self.energy)
        
    def view_update(self):
        self.text_input.delete(0, "end")
        self.text_input.insert(0, self.myDate.toString())

        self.text_energy.delete(0, "end")
        self.text_energy.insert(0, self.myPet.energy)

        self.text_hunger.delete(0, "end")
        self.text_hunger.insert(0, self.myPet.hunger)
    

root = tk.Tk()
window = TestGUI(root)
root.geometry('800x500')
window.mainloop()
