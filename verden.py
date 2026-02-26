from rutenett import Rutenett
from celle import Celle
class Verden:
    def __init__(self, rader, kolonner):
        # konstruktøren skal ta inn antall rader og kolonner som parametere
        self._rader = rader
        self._kolonner = kolonner

        # skal også opprette en instans av klassen Rutenett som lagres i instansvariabel
        self._rutenett = Rutenett(rader, kolonner)

        # trenger instansvariabel _generasjonsnummer for å holde styr på antall generasjoner
        # den skal settes til lik 0
        self._generasjonsnummer = 0

        # rutenettet skal fylles med tilfeldige celler og koble cellene sammen
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):
        # metoden skal tegne rutenettet i tillegg til å skrive ut generasjonsnummeret og antall levende celler som er igjen
        self._rutenett.tegn_rutenett()
        print(f"Generasjonsnummeret: {self._generasjonsnummer}\nAntall levende celler igjen: {self._rutenett.antall_levende()}")

    def oppdatering(self): 
        # gå gjennom alle celler i rutenettet og telle levende naboer for hver celle
       
        for rad in self._rutenett.hent_alle_celler():
                rad.tell_levende_naboer()
        
        
        # gå gjennom alle celler i rutenettet på nytt og oppdatere status på hver celle
    
        for rad in self._rutenett.hent_alle_celler():
            rad.oppdater_status()

        # oppdaterer telleren for antall generasjoner
        self._generasjonsnummer += 1