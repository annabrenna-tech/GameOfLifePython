from verden import Verden

def hovedprogram():
    # brukeren blir spurt om å oppgi dimensjoner på spillebrettet
    rad = int(input("Hvor mange rad skal spillebrettet ha?\n"))
    kol = int(input("Hvor mange kolonner skal spillebrettet ha?\n"))

    # oppretter "verden" og tegne "nulte" generasjon
    verden = Verden(rad, kol)
    verden.tegn()

    # Ved hjelp en menyløkke og input skal brukeren deretter kunne velge å oppgi en tom linje for å gå videre til neste steg, eller skrive inn bokstaven “q” for å avslutte programmet
    svar = ""
    while svar != "q" and svar == "":
        svar = input("Press enter for å fortsette. Skriv inn 'q' og trykk enter for å avslutte\n")
        # hver gang brukeren oppgir at de ønsker å fortsette skal oppdatering-metoden kalles på og deretter tegne verden på nytt
        if svar == "":
            verden.oppdatering()
            # skrives ut en linje som beskriver hvilken generasjon som beskriver hvilken generasjon som vises og hvor mange celler som lever for øyeblikket
            verden.tegn()
        

# starte hovedprogrammet
hovedprogram()