
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
        self.place()
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
        print_button.pack(side="bottom")
        print_button.bind("<ButtonRelease>", self.model_next_day)
        print_button.bind("<Return>", self.model_next_day)
        print_button.bind("<space>", self.model_next_day)

        walk_button = tk.Button(self, text="Walk")
        walk_button.pack(side="bottom")
        walk_button.bind("<ButtonRelease>", self.walk)
        walk_button.bind("<Return>", self.walk)
        walk_button.bind("<space>", self.walk)

        volumeUPButton = tk.Button(self, text="+")
        volumeUPButton.pack(side="bottom")
        volumeUPButton.bind("<ButtonRelease>", self.volumeUP)

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

        # UI elements #
        petNameLabel = tk.Label(self, text=self.name)
        petNameLabel.config(font=("Comic Sans MS", 44))
        petNameLabel.pack(side="top")

        dateLabel = tk.Label(self, text="Current Date")
        dateLabel.config(font=("Comic Sans MS", 25))
        dateLabel.pack(side="top")
        self.text_input = tk.Entry(self)
        self.text_input.insert(0, self.myDate.toString())
        self.text_input.pack(side="top")

        energyLabel = tk.Label(self, text="Energy:")
        energyLabel.config(font=("Comic Sans MS", 25))
        energyLabel.pack(side="left")
        self.text_energy = tk.Entry(self)
        self.text_energy.insert(0, self.myPet.energy)
        self.text_energy.pack(side="left")

        hungerLabel = tk.Label(self, text="Hunger:")
        hungerLabel.config(font=("Comic Sans MS", 25))
        hungerLabel.pack(side="left")
        self.text_hunger = tk.Entry(self)
        self.text_hunger.insert(0, self.myPet.hunger)
        self.text_hunger.pack(side="bottom")

        # Audio control #
        gameVolume = 0.0
        pygame.mixer.init()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('menumusic.wav'), loops=-1)
        pygame.mixer.music.set_volume(gameVolume)
        #pygame.mixer.music.load('menumusic.wav')
        #pygame.mixer.music.play(loops=-1)


    def volumeUP(self, event):
        gameVolume = gameVolume + 0.1

    def walk(self, event):
        self.myPet.walk()
        self.model_next_day()

    def model_next_day(self, event):
        self.myDate.setToNextDate()
        self.myPet.setToNextHour()

        # Death checks #
        if (self.myPet.deathHungerOver() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af mangel på mad...")
        if (self.myPet.deathEnergyOver() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af den ikke fik nok motion.")
        if (self.myPet.deathEnergyUnder() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af du gav det for meget mad")
        if (self.myPet.deathHungerUnder() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af for meget motion")
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
