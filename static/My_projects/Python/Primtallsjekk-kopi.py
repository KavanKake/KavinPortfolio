# Importerer matte
import math

#Definer primtall
def er_primtall(tall):
    if tall < 2:
        return False
    elif tall == 2:
        return True
    elif tall % 2 == 0:
        return False

    grense = int(math.sqrt(tall)) + 1
    for i in range(3, grense, 2):
        if tall % i == 0:
            return False

    return True

# Ber om et primtall
primtall_sjekk  = int(input("Skriv et tall du vil sjekke om er et primtall"))

# kjører tallet i funksjoen over for å sjekke om det er primtall
if er_primtall(primtall_sjekk):
    print(f"{primtall_sjekk} er et primtall.")
else:
    print(f"{primtall_sjekk} er ikke et primtall.")
