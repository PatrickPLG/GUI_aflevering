
import tkinter as tk
import date
import pet
from tkinter import simpledialog
from tkinter import messagebox
import pygame
from pygame import mixer



class TestGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main_window = master
        self.main_window.title("Pet")
        self.pack()
        self.grid()
        self.petName()

    def petName(self):
        self.petNameInput = simpledialog.askstring("Pet name", "Set pet name")
        if (self.petNameInput == ""):
            self.petNameInput = "Missingno"
        self.name = self.petNameInput
        self.controller_init()
        self.model_init()
        self.view_init()

    def controller_init(self):

        # Event handler #
        print_button = tk.Button(self, text="Next")
        print_button.grid(row=5, column=1)
        print_button.bind("<ButtonRelease>", self.model_next_day)
        print_button.bind("<Return>", self.model_next_day)
        print_button.bind("<space>", self.model_next_day)

        walk_button = tk.Button(self, text="Walk")
        walk_button.grid(row=5, column=2)
        walk_button.bind("<ButtonRelease>", self.walk)
        walk_button.bind("<Return>", self.walk)
        walk_button.bind("<space>", self.walk)

        eat_button = tk.Button(self, text="Eat")
        eat_button.grid(row=5, column=3)
        eat_button.bind("<ButtonRelease>", self.eat)
        eat_button.bind("<Return>", self.eat)
        eat_button.bind("<space>", self.eat)

        infoText = ["Velkommen til spillet",
                    "I dette spil skal du passe på din egen hund",
                    "Du kan give den mad, gå ture med den eller vælge ikke at gøre noget",
                    "MEN! Du skal huske på to ting!",
                    "Sult og Energy må ikke komme over 300",
                    "Sult og Energy må ikke komme under 0",
                    "Hvis dette sker dør dit dyr!",
                    " ",
                    "Held og lykke!"]

        self.startInfo = messagebox.showinfo("Information about game",
                                             "\n".join(infoText))

    def model_init(self):
        self.myDate = date.Date(20, 5, 2020)
        self.myPet = pet.Pet(0, 0, 0)

    def view_init(self):

        dateLabel = tk.Label(self, text="Current Date")
        dateLabel.config(font=("Comic Sans MS", 25))
        dateLabel.grid(row=1, column=1)
        self.text_input = tk.Entry(self)
        self.text_input.insert(0, self.myDate.toString())
        self.text_input.grid(row=1, column=2)

        energyLabel = tk.Label(self, text="Energy:")
        energyLabel.config(font=("Comic Sans MS", 25))
        energyLabel.grid(row=1, column=4)
        self.text_energy = tk.Entry(self)
        self.text_energy.insert(0, self.myPet.energy)
        self.text_energy.grid(row=1, column=5)

        hungerLabel = tk.Label(self, text="Hunger:")
        hungerLabel.config(font=("Comic Sans MS", 25))
        hungerLabel.pack(row=1, column=7)
        self.text_hunger = tk.Entry(self)
        self.text_hunger.insert(0, self.myPet.hunger)
        self.text_hunger.pack(side="bottom")

        # UI elements #
        petNameLabel = tk.Label(self, text=self.name)
        petNameLabel.config(font=("Comic Sans MS", 44))
        petNameLabel.pack(side="top")

        # Audio control #
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        pygame.mixer.init()
        #pygame.mixer.Channel(0).play(pygame.mixer.Sound('menumusic.wav'), loops=-1)
        sound1 = pygame.mixer.Sound('menumusic.wav')
        sound1.set_volume(0.1)
        sound1.play()

    def walk(self, event):
        self.myPet.walk()
        self.model_next_day()

    def eat(self, event):
        self.myPet.eat()
        self.model_next_day()

    def model_next_day(self, event=None):
        self.myDate.setToNextDate()
        self.myPet.setToNextHour()

        # Death checks #
        if (self.myPet.deathHungerOver() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af mangel på mad...")
        if (self.myPet.deathEnergyOver() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af den ikke fik nok motion.")
        if (self.myPet.deathEnergyUnder() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af for meget motion")
        if (self.myPet.deathHungerUnder() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af du gav det for meget mad")
        # ------------

        self.view_update()

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
