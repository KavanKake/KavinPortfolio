def multiplikasjon(a,b):
    a*b
def divisjon(a, b):
    if b == 0:
        return "Kan ikke dele på null"
    return a / b
def addisjon(a,b):
    a+b
def subtraksjon(a,b):
    a-b



def hovedprogram():
    desimaler = int(input("Angi antall desimaler for resultatene: "))

    while True: 
        print("\nVelg en operasjon:")
        print("1. Addisjon")
        print("2. Subtraksjon")
        print("3. Multiplikasjon")
        print("4. Divisjon")
        print("5. Avslutt")

        valg = input("Skriv inn operasjonens nummer (1/2/3/4/5): ")
        
        if valg == '5':
            print("Avslutter programmet.")
            break
        
        if valg not in ['1', '2', '3', '4']:
            print("Ugyldig valg. Prøv igjen.")
            continue
        
        a = float(input("Skriv inn det første tallet: "))
        b = float(input("Skriv inn det andre tallet: "))
        
        if valg == '1':
            resultat = addisjon(a, b)
        elif valg == '2':
            resultat = subtraksjon(a, b)
        elif valg == '3':
            resultat = multiplikasjon(a, b)
        elif valg == '4':
            resultat = divisjon(a, b)   

        format_string = "{:.%df}" % desimaler
        resultat_str = format_string.format(resultat)
        print("Resultat:", resultat_str)

hovedprogram()