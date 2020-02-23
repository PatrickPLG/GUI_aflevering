'''
 - Pet game, where you can feed and walk your pet
 - Made by PatrickPLG og Klint02
 - version 2.0 Public Release
'''


# Library and file imports
import tkinter as tk
import date
import pet
import TidTest
import os
from tkinter import simpledialog
from tkinter import PhotoImage, messagebox
import pygame
from pygame import mixer

class petGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main_window = master
        self.main_window.title("Pet")
        self.pack()
        self.grid()
        self.petName()

    def petName(self):
        # Makes an variable called self.petNameInput which is the name used in the game
        self.petNameInput = simpledialog.askstring("Pet name", "Set pet name")
        # If self.petNameInput is empty
        if (self.petNameInput == ""):
            self.petNameInput = "Missingno"
        self.name = self.petNameInput
        # Runs controller_init(), model_init() and view_init()
        self.controller_init()
        self.model_init()
        self.view_init()

    def controller_init(self):

        # Event handler #
        # Each button is binded to a function inside the program
        print_button = tk.Button(self, text="Next")
        print_button.grid(row=5, column=6)
        print_button.bind("<ButtonRelease>", self.model_next_hour)
        print_button.bind("<Return>", self.model_next_hour)
        print_button.bind("<space>", self.model_next_hour)

        walk_button = tk.Button(self, text="Walk")
        walk_button.grid(row=6, column=6)
        walk_button.bind("<ButtonRelease>", self.walk)
        walk_button.bind("<Return>", self.walk)
        walk_button.bind("<space>", self.walk)

        eat_button = tk.Button(self, text="Eat")
        eat_button.grid(row=7, column=6)
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
        # Imports the classes from the other files
        self.myDate = date.Date(20, 5, 2020)
        self.tidTest = TidTest.time(1)
        self.myPet = pet.Pet(0, 0, 0)

    def view_init(self):
        # UI elements #
        # Creates a Tkinter PhotoImage with a given path and places it by using the .place command
        dogPhoto = tk.PhotoImage(file=r"Assets/Dog graphics/Dog4.gif")
        dogLabel = tk.Label(image=dogPhoto,)
        dogLabel.image = dogPhoto
        dogLabel.place(x=380, y=70)

        # Creates Tkinter Labels and Entries and places them using the .grid command system
        # For the Labels it usus the .insert command to insert information from other parts of the program
        dateLabel = tk.Label(self, text="Current Date")
        dateLabel.config(font=("Fixedsys", 25))
        dateLabel.grid(row=1, column=1)
        self.text_input = tk.Entry(self)
        self.text_input.insert(0, self.myDate.toString())
        self.text_input.grid(row=2, column=1)

        timeLabel = tk.Label(self, text="Current Hour")
        timeLabel.config(font=("Fixedsys", 25))
        timeLabel.grid(row=3, column=1)
        self.text_hour = tk.Entry(self)
        self.text_hour.insert(0, self.tidTest.toString())
        self.text_hour.grid(row=4, column=1)

        energyLabel = tk.Label(self, text="Energy:")
        energyLabel.config(font=("Fixedsys", 25))
        energyLabel.grid(row=5, column=1)
        self.text_energy = tk.Entry(self)
        self.text_energy.insert(0, self.myPet.energy)
        self.text_energy.grid(row=6, column=1)

        hungerLabel = tk.Label(self, text="Hunger:")
        hungerLabel.config(font=("Fixedsys", 25))
        hungerLabel.grid(row=7, column=1)
        self.text_hunger = tk.Entry(self)
        self.text_hunger.insert(0, self.myPet.hunger)
        self.text_hunger.grid(row=8, column=1)

        petNameLabel = tk.Label(self, text=self.name)
        petNameLabel.config(font=("Fixedsys", 25))
        petNameLabel.grid(row=1, column=2, padx=100)

        # Audio control #
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
        pygame.mixer.init()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Assets/menumusic.wav'), loops=-1)
        pygame.mixer.music.set_volume(0.1)

    # Makes the pet walk and it skips to the next hour
    def walk(self, event):
        self.myPet.walk()
        self.model_next_hour()

    # Makes the pet eat and it skips to the next hour
    def eat(self, event):
        self.myPet.eat()
        self.model_next_hour()

    def model_next_hour(self, event=None):
        # Sets new hour and checks if the time is over 24
        self.tidTest.setToNextDate()
        self.myPet.setToNextHour()
        if (self.tidTest.checkDayOverflow() == True):
            self.model_next_day()

        # Death checks #
        if (self.myPet.deathHungerOver() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af mangel på mad...")
            self.myDate = date.Date(20, 5, 2020)
            self.tidTest = TidTest.time(1)
            self.myPet = pet.Pet(0, 0, 0)
        if (self.myPet.deathEnergyOver() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af den ikke fik nok motion.")
            self.myDate = date.Date(20, 5, 2020)
            self.tidTest = TidTest.time(1)
            self.myPet = pet.Pet(0, 0, 0)
        if (self.myPet.deathEnergyUnder() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af for meget motion")
            self.myDate = date.Date(20, 5, 2020)
            self.tidTest = TidTest.time(1)
            self.myPet = pet.Pet(0, 0, 0)
        if (self.myPet.deathHungerUnder() == True):
            messagebox.showwarning("Your pet died", self.name + " døde på grund af du gav det for meget mad")
            self.myDate = date.Date(20, 5, 2020)
            self.tidTest = TidTest.time(1)
            self.myPet = pet.Pet(0, 0, 0)
        
        # Runs view_update()
        self.view_update()

    # Sets a new date and updates the ui
    def model_next_day(self, event=None):
        self.myDate.setToNextDate()
        self.view_update()

    # Updates to the ui
    def view_update(self):
        self.text_input.delete(0, "end")
        self.text_input.insert(0, self.myDate.toString())

        self.text_hour.delete(0, "end")
        self.text_hour.insert(0, self.tidTest.toString())

        self.text_energy.delete(0, "end")
        self.text_energy.insert(0, self.myPet.energy)

        self.text_hunger.delete(0, "end")
        self.text_hunger.insert(0, self.myPet.hunger)


root = tk.Tk()
window = petGUI(root)
root.geometry('800x300')
window.mainloop()
