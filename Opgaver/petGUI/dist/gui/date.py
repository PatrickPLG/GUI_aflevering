# En instans repræsenterer en dato.
class Date:
    # Konstruktør til at oprette en dato
    def __init__(self, day, month, year):
        # Variable til repræsentation af dato
        self.day = day
        self.month = month
        self.year = year
        
    # Ændrer datoen til næste dag
    def setToNextDate(self):
        self.day = self.day + 1
        self.checkDayOverflow()

    # Returnerer datoen som en streng
    def toString(self):
        return str(self.day) + "-" + str(self.month)\
               + "-" + str(self.year)

    # Kontrollerer for specialtilfælde hvor day
    # overskrider antal dage i måneden
    def checkDayOverflow(self):
        if (self.day > self.daysInMonth()):
            self.day = 1
            self.month = self.month + 1
            self.checkMonthOverflow()

    # Kontrollerer for specialtilfælde med month > 12
    def checkMonthOverflow(self):
        if (self.month > 12):
            self.month = 1
            self.year = self.year + 1

    # Returnerer antal dage i måneden
    def daysInMonth(self):
        daysInMonth = [31, 28, 31, 30, 31, 30,\
                       31, 31, 30, 31, 30, 31]
        result = daysInMonth[self.month-1]
        # Specialtilfælde ved skudår
        if (self.month == 2 and self.isLeapYear()):
            result = result + 1
        return result

    # Returnerer true hvis og kun hvis det er skudår
    def isLeapYear(self):
        return (self.divides(4, self.year) and \
                not self.divides(100, self.year) \
                or self.divides(400, self.year))

    # Returnerer true hvis og kun hvis a går op i b
    def divides(self, a, b):
        return b % a == 0
