"""

Version 2.1 - Dato: 13-9-2019
Forfatter: Patrick Gravengaard
Formål: En digitalt hund, som man man skal passe på, hvor man kan give den mad og gå ture med den.

"""

import time

class Pet:
	#Konstruktør til at oprette et kæledyr
	def __init__(self, hour, energy, hunger):
		self.hour = 5
		self.energy = 80
		self.hunger = 90
		self.weekDayIndex = 0



	# Lader tiden gå, hvor der bliver plusset 1 time til self.hour, plusset 20 til self.energy og plusset 10 til self.hunger
	def setToNextHour(self):
		#self.hour = self.hour + 1
		self.energy = self.energy + 20
		self.hunger = self.hunger + 10

	#Opretter et array som indeholder alle ugedagene
	def weekDayName(self):
		weekDay = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
		result = weekDay[self.weekDayIndex]
		return result

	#Tjekker om klokken er over 21 og sætter klokken til 6 hvis dette er sandt 
	def checkHourOverFlow(self):
		if (self.hour > 21):
			print("Klokken er 21 og " + name + " ligger sig til at sove")
			time.sleep(2)
			for sleep in range(3):
				print("zZzzzZZ")
				time.sleep(2)
			print("")
			#Plusser 1 til weekDayIndex,som gør det bliver en ny dag
			self.weekDayIndex = self.weekDayIndex + 1
			#Hvis ugedagene er over 6 (Søndag), bliver det til 0 (Mandag)
			if (self.weekDayIndex > 6):
				self.weekDayIndex = 0
			self.hour = 6

	'''
	#Tjekker om dyret dyr pga. forskellige årsager og restarter herefter spillet, med start værdier til variablerne
	def checkDeath(self):
		if (self.hunger >= 300):
			print(name + " døde på grund af mangel på mad...")
			print("")
			print("Starter nyt spil.")
			time.sleep(5)
			for clear in range(50):
				print("")
			self.hour = 5
			self.energy = 100
			self.hunger = 100
		elif (self.energy >= 300):
			print(name + " døde på grund af den ikke fik nok motion.")
			print("")
			print("Starter nyt spil.")
			time.sleep(5)
			for clear in range(50):
				print("")
			self.hour = 6
			self.energy = 100
			self.hunger = 100
		elif (self.hunger <= 0):
			print(name + " døde på grund af du gav det for meget mad")
			print("")
			print("Starter nyt spil.")
			time.sleep(5)
			for clear in range(50):
				print("")
			self.hour = 6
			self.energy = 100
			self.hunger = 100
		elif (self.energy <= 0):
			print(name + " døde på grund af for meget motion")
			print("")
			print("Starter nyt spil.")
			time.sleep(5)
			for clear in range(50):
				print("")
			self.hour = 6
			self.energy = 100
			self.hunger = 100
			'''
	def deathHungerOver(self):
		if (self.hunger >= 300):
			self.hour = 5
			self.energy = 100
			self.hunger = 100
			return True
		else:
			return False
	def deathEnergyOver(self):
		if (self.energy >= 300):
			self.hour = 6
			self.energy = 100
			self.hunger = 100
			return True
		else:
			return False
	def deathHungerUnder(self):
		if (self.hunger <= 0):
			self.hour = 6
			self.energy = 100
			self.hunger = 100
			return True
		else:
			return False
	def deathEnergyUnder(self):
		if (self.energy <= 0):
			self.hour = 6
			self.energy = 100
			self.hunger = 100
			return True
		else:
			return False

	def petName(self):
		name = "Allo"
		self.name = name
		return self.name

	#Printer self.hour, self.energy, self.hunger og weekDayName
	def toString(self):
		return "Dag: " + str(self.weekDayName()) + " - " +  "Tid: " + str(self.hour) + " - " + "Energy: " + str(self.energy)\
			  + " - " + "Sult: " + str(self.hunger)

	#Spiser, hvilket minusser 60 for værdien af self.hunger
	def eat(self):
		self.hunger = self.hunger - 60


	#Går, som minusser 70 fra værdien af self.energy
	def walk(self):
		self.energy = self.energy - 70

	#Spørgsmålene som brugeren ville blive stillet, som herefter, efter brugerens indtastede valg vil køre en funktion
	def question(self):
		choice = input("Hvad vil du gøre? Ingen ting/Spise/Gå?: ")
		if choice == "Ingen ting" or choice == "ingen ting":
			print("Du gjorde ingen ting")
		elif choice == "Spise" or choice == "spise":
			print("Du giver " + self.name + " mad")
			self.eat()
		elif choice == "Gå" or choice == "gå":
			print("Du går en tur med " + self.name )
			self.walk()
		elif choice == "":
			print("Du gjorde ingen ting")

#Kæledyret
Pets = [
	Pet(0, 0, 0)
]



'''

#"Startmenuen", som bliver vist når programmet køres.
for p in Pets:
	start = True
	if (start == True):
		print("")
		print("Velkommen til spillet")
		print("")
		print("I dette spil skal du passe på din egen hund")
		print("")
		print("Du kan give den mad, gå ture med den eller vælge ikke at gøre noget")
		print("")
		print("MEN! Du skal huske på to ting!")
		print("")
		print("Sult og Energy må ikke komme over 300")
		print("Sult og Energy må ikke komme under 0")
		print("Hvis dette sker dør dit dyr!")
		print("")
		print("Held og lykke!")
		print("")
		print("Tryk på ENTER for at starte spillet")
		startButton = input()
		if startButton == "":
			for clear in range(50):
				print("")
			print("Hvad vil du kalde din hund?")
			name = input()
			for clear in range(50):
				print("")
			print("Spillet begynder om 5 sekunder!")
			time.sleep(5)
			for clear in range(50):
				print("")
			start = False

	#Kører efter "startmenuen" og det er det der kører alle funktionerne som er lavet længere oppe i koden
	if (start == False):
		while True:
			p.setToNextHour()
			p.checkDeath()
			p.checkHourOverFlow()
			print(p.toString())
			p.question()
			print("")
'''