# Oppretter en class som definerer 
class Bankkonto:
    def __init__(self, kontonummer, saldo=0):
        self.kontonummer = kontonummer
        self.saldo = saldo

# Sjekker om tallet er postivt så legger den til. HVis negativ sier den at tallet må være positivt. 
    def innskudd(self, beløp):
        if beløp > 0:
            self.saldo += beløp
            print(f"Innskudd på {beløp} kroner vellykket. Ny saldo: {self.saldo} kroner.")
        else:
            print("Feil: Innskuddsbeløpet må være positivt.")

# Hvordan uttak fungerer, starter med at uttaksnummeret må være postiv, så om du har nok på kontoen, så sier den om den om beløpet er negativ hvis det er. 
    def uttak(self, beløp):
        if 0 < beløp <= self.saldo:
            self.saldo -= beløp
            print(f"Uttak på {beløp} kroner vellykket. Ny saldo: {self.saldo} kroner.")
        elif beløp > self.saldo:
            print("Feil: Du har ikke nok penger på kontoen.")
        else:
            print("Feil: Uttaksbeløpet må være positivt.")

# Forteller hvor mye saldoen er på etter innskudd eller uttak
    def hent_saldo(self):
        return self.saldo


# Du skriver inn hva kontonummeret ditt er, sammen med hvor mye du har på den. 
banknummer = int(input("Hva er kontonummer din? "))
nåværende_saldo = int(input("Hvor mye har du på kontoen din nå?"))
konto1 = Bankkonto(banknummer, nåværende_saldo)
print(f"Konto med kontonummer {konto1.kontonummer} har blitt opprettet med saldo {konto1.hent_saldo()} kroner.")


# Koden spør deg om du skal legge til eller ta ut penger fra kontoen din
spørsmål = input("Ønsker du innskudd eller uttak ")
if spørsmål == "innskudd": 
    beløp = int(input("Hvor mye ønsker du å putte inn? ")) 
    konto1.innskudd(beløp)
elif spørsmål == "uttak": 
    beløp = int(input("Hvor mye ønsker du å ta ut? "))
    konto1.uttak(beløp)

#Koden sier hva saldoen er på nå, etter innskudd eller uttak
print(f"Nåværende saldo: {konto1.hent_saldo()} kroner.")

