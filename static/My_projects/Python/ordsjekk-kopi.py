def sjekk_ord(ordet):
    # Hvor mange bokstaver inneholder ordet?
    antall_bokstaver = len(ordet)

    # Er første og siste bokstav like?
    er_like = ordet[0] == ordet[-1]

    # Hvor mange 's'-er og 't'-er inneholder ordet?
    antall_s = ordet.count('s')
    antall_t = ordet.count('t')

    er_palindrom = ordet == ordet[::-1]

    # Skriv ut resultatene
    print(f"Ord: {ordet}")
    print(f"Antall bokstaver: {antall_bokstaver}")
    print(f"Er første og siste bokstav like? {er_like}")
    print(f"Antall 's'-er: {antall_s}")
    print(f"Antall 't'-er: {antall_t}")
    print(f"Er et palindrom? {er_palindrom}")
    print()

# Ta inn en streng av ord fra brukeren
input_streng = input("Skriv inn flere ord, separert med mellomrom: ")

# Del opp strengen i en liste av ord
ordliste = input_streng.split()

# Utfør sjekk for hvert ord i listen
for ordet in ordliste:
    sjekk_ord(ordet)









