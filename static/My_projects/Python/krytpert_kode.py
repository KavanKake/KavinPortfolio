def krypter_melding(melding, forskyvning):
    kryptert_melding = ""

    for bokstav in melding:
        if bokstav.isalpha():  # Sjekker om tegnet er en bokstav
            # Beregner den krypterte bokstaven ved å forskyve i alfabetet
            kryptert_bokstav = chr((ord(bokstav.lower()) - ord('a') + forskyvning) % 26 + ord('a'))
            # Bevarer original bokstavens case
            if bokstav.isupper():
                kryptert_bokstav = kryptert_bokstav.upper()
            kryptert_melding += kryptert_bokstav
        else:
            # Beholder ikke-bokstaver uendret
            kryptert_melding += bokstav

    return kryptert_melding

# Hovedprogram
ord_for_kryptering = input("Skriv inn ordene du vil kryptere: ")
forskyvning = int(input("Skriv inn antall forskyvninger: "))

kryptert_resultat = krypter_melding(ord_for_kryptering, forskyvning)

print(f"Den krypterte meldingen er: {kryptert_resultat}")
