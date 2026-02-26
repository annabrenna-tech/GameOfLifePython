 
from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        # Konstruktøren tar imot dimensjoner på rutenettet og lagrer disse i instansvariablene self._ant_rader og self._ant_kolonner
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        # ny instansvariabel _rutenett i form av en todimensjonal liste
        self._rutenett = []
        self._lag_tomt_rutenett()  # denne metoden må kalles i konstruktøren for å opprette rutenett

    def _lag_tomt_rutenett(self):
        # setter rader laget av _lag_tom_rad sammen i en ytre liste
        for _ in range(self._ant_rader):
            self._rutenett.append(self._lag_tom_rad())
        
    def _lag_tom_rad(self):
        # lager en enkel liste med like mange None-verdier som det skal være kolonner
        kolonner = []
        x = None
        for _ in range(self._ant_kolonner):
            kolonner.append(x)
        return kolonner
    
    def fyll_med_tilfeldige_celler(self):
        # går gjennom rutenettet og sørger for at et tilfeldig antall celler får status "levende"
        # bruk radint greie for å få velge et tilfeldig antall celler
        for rad in range(self._ant_rader):
            for kolonner in range(self._ant_kolonner):
                ny = self.lag_celle(rad, kolonner)
                if randint(0, 2) == 1:
                    ny.sett_levende()


    def lag_celle(self, rad, kol):
        # oppretter en instans av klassen Celle og legger det inn på en plass i den nøstede lista ut fra rad og kol
        nycelle = Celle()
        self._rutenett[rad][kol] = nycelle
        return nycelle
        

    def hent_celle(self, rad, kol):
        # tar imot en celles koordinater i rutenettet og returnerer cellen til den gitte posisjonen
       
        if rad < 0 or rad >= self._ant_rader:
            return None
        elif kol < 0 or kol >= self._ant_kolonner:
            return None
        else:
            return self._rutenett[rad][kol]
        
    def tegn_rutenett(self):
        # metoden skal bruke en nøstet for løkke for å skrive ut hvert element i rutenettet
        for rad in self._rutenett:
            for kolonner in rad:
                print(kolonner.hent_status_tegn(), end="")  # avslutter utskriften med en tom streng uten linjeskift
            print()
        for _ in range(2):
            print()  # får mellomrom mellom tegn da rutenettet printes ut
        
    def _sett_naboer(self, rad, kol):
        # metoden tar i mot en celles koordinater og sette referanser til alle instanser av klassen Celle som er nabo for den gitte Celle instansen
        # bruker hent_celle til å hente celler uten å få feilmeldinger for ulovlig indekser
        celle = self.hent_celle(rad, kol)
        naboer = []  # opprettet en tom liste som naboer skal legges til
        naboer.append(self.hent_celle(rad-1, kol-1))
        naboer.append(self.hent_celle(rad-1, kol))
        naboer.append(self.hent_celle(rad-1, kol+1))
        naboer.append(self.hent_celle(rad, kol-1))
        naboer.append(self.hent_celle(rad, kol + 1))
        naboer.append(self.hent_celle(rad+1, kol-1))
        naboer.append(self.hent_celle(rad+1, kol))
        naboer.append(self.hent_celle(rad+1, kol+1))
        
        # går gjennom noboer liste og hvis indeks er gyldig eller != None skal metoden legg_til_nabo() kalles
        for nabo in naboer: 
            if nabo != None:
                celle.legg_til_nabo(nabo)

    def koble_celler(self):
        # metoden bruker en nøstet for-løkke for å gå gjennom rutenettet og kalle på _sett_naboer() for hver plass
        for rad in range(self._ant_rader):
            for kolonner in range(self._ant_kolonner):
                self._sett_naboer(rad, kolonner)

    def hent_alle_celler(self):
        # returnerer en enkel liste med alle instanser av klassen Celle i rutenettet
        celle_liste = []
        for rad in self._rutenett:
            for kolonner in rad:
                celle_liste.append(kolonner)
        return celle_liste

    def antall_levende(self):
        # returnerer antall levende celler i rutenettet
        teller = 0
        # går gjennom rutenettet og øke en teller for hver levende celler som finnes
        for rad in self._rutenett:
            for kolonner in rad:
                if kolonner.er_levende():
                    teller += 1
        return teller