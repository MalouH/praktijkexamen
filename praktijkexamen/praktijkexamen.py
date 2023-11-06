# leeftijd van de gebruiker
leeftijd = int(input("Wat is je leeftijd? Voer het aantal jaren in:"))

# werkstatuut van de gebruiker
werkstatuut = input ("Wat is je werkstatuut? Voer in: medewerker, zelfstandige of ambtenaar:")

# functie die berekent en toont of gebruiker pensiengerechtigd is en hoeveel hij krijgt op basis van zijn leeftijd
def pensioenbedrag(leeftijd,werkstatuut):
    #resterende werkjaren indien gebruiker nog niet pensioengerechtigd is
    resterende_werkjaren= 65 - leeftijd
    if leeftijd >=65 and leeftijd <70:
        if werkstatuut == "medewerker": 
            return "Je krijgt €350 per week."
        if werkstatuut == "zelfstandige": 
            return "Je krijgt €300 per week."
        if werkstatuut == "ambtenaar": 
            return "Je krijgt €370 per week."
    if leeftijd >= 70:
        if werkstatuut == "medewerker": 
            return "Je krijgt €370 per week."
        if werkstatuut == "zelfstandige": 
            return "Je krijgt €315 per week."
        if werkstatuut == "ambtenaar": 
            return "Je krijgt €395 euro per week"
    else:
        return f"Van werken word je gelukkig, je mag nog {resterende_werkjaren} jaar genieten van je baan."
print (pensioenbedrag(leeftijd, werkstatuut))