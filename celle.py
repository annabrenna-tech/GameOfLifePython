class Celle:
    # Konstruktør
    def __init__(self):
        # konstruktør for klassen som oppretter cellen med _status “doed” som utgangspunkt
        self._status = "doed"
        # instansvariablene _naboer som settes lik en tom liste, og _ant_levende_naboer som settes lik 0
        self._naboer = []
        self._ant_levende_naboer = 0
    
    def sett_doed(self):
        # setter status til "doed"
        self._status = "doed"
        return self._status

    def sett_levende(self):
        # setter status til "levende"
        self._status = "levende"
        return self._status

    def er_levende(self):
        # returnerer True hvis cellen er levende og False ellers
        return self._status == "levende"
     

    def hent_status_tegn(self):
        # returnerer en tegn_representasjon av cellens status
        if self.er_levende():
            return "O"
        else:
            return "."

    def legg_til_nabo(self, nabo):
        # legger nabo til naboer lista
        self._naboer.append(nabo)

    def tell_levende_naboer(self):  
        # går gjennom naboer lista og teller antall levende naboer
        self._ant_levende_naboer = 0  # må nullstille teller hver gang vi kalle på metoden, ellers skal den fortsette å legg 1 hver gang metoden kalles
        for nabo in self._naboer:
            if nabo.er_levende():
                self._ant_levende_naboer += 1
            
    def oppdater_status(self):
        # endrer statusen til en celle basert på antall levende naboer
        if self._ant_levende_naboer == 3:
            self.sett_levende()
        elif self._ant_levende_naboer < 2:
            self.sett_doed()
        elif self._ant_levende_naboer > 3:
            self.sett_doed()
   