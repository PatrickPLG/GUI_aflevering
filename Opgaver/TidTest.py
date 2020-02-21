# En instans repræsenterer en dato.
class time:
    # Konstruktør til at oprette en dato
    def __init__(self, hour):
        # Variable til repræsentation af dato
        self.hour = hour
        
    # Ændrer datoen til næste dag
    def setToNextDate(self):
        self.hour = self.hour + 1
        self.checkDayOverflow()

    # Returnerer datoen som en streng
    def toString(self):
        return str(self.hour)

    # Kontrollerer for specialtilfælde hvor day
    # overskrider antal dage i måneden
    def checkDayOverflow(self):
        if (self.hour > 21):
            self.hour = 1
            return True
        else:
            return False