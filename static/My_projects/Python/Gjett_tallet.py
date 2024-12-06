"""Oppgave 3"""
# Importerer "random" og setter tallene den kan være mellom 0 og 10. 
import random
random_tall= random.randint(0,10)

"""
Koden gir deg tre forsøk og ber deg om å velge et tall mellom 0 og 10. Den setter definisjonsmengden på 0 - 10 og alle andre tall er ugyldig
Hvis du klarer å gjette riktig får du vite det, hvis ikke får du hint og kan gjøre det på nytt. 
"""

for i in range(3):
    player = float(input("gjett et tall mellom 0 og 10 "))
    print("forsøk = ", i+1)
    if player < 0 and player > 11: 
        print("tall er ugyldig, prøv på nytt!")
    if random_tall == player: 
        print("du klarte det!")
        break
    else: 
        print ("Feil tall, hint er : hvis man opphøyer tallet med 2 får man: ", random_tall**2)


# Hvis du klarte å gjette tallet får du en gladmelding og kan starte på nytt, men hvis du taper, får du en annen melding. 
if player == random_tall: 
    print("----------------")
    print("Gratulerer, start på nytt for en runde til!")
else: 
    print("beklager, du feilet! Start på nytt for en ny runde")



