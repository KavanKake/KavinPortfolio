"""Oppgave 2""" 
# Importerer random 
import random

def stein_saks_papir():
    valg = ["stein", "saks", "papir"]
    monster_poeng = 0 
    spiller_poeng = 0
    print("best av tre")
    while monster_poeng != 2 or spiller_poeng != 2:
        bruker_input = input("Velg stein, saks eller papir").lower()
        monstervalg_valg = random.choice(valg)
            
        if bruker_input in valg:
            print(f"Brukeren valgte: {bruker_input}")
            print(f"monsteret valgte: {monstervalg_valg}")
            if bruker_input == monstervalg_valg:
                print("Uavgjort!")
            elif (bruker_input == "stein" and monstervalg_valg == "saks") or (bruker_input == "saks" and monstervalg_valg == "papir") or (bruker_input == "papir" and monstervalg_valg == "stein"):
                print("Du vant!")
                spiller_poeng =+ 1 
                print("du har: ",spiller_poeng, "og monsteret har: ", monster_poeng )
                
            else:
                print("monsteret  vant!")
                monster_poeng =+1
        else:
            print("Ugyldig valg. Vennligst velg stein, saks eller papir.")
    if spiller_poeng == 2: 
        print("spiller vant")
        print("Du fikk skattene")
    else: 
        print("monster vant")
        print("Monsteret følte synd på deg og ga skatten likeveld")

# Kjører funksjoen over
stein_saks_papir()




