def dekrypter_melding(kryptert_melding, forskyvning):
    dekryptert_melding = ""

    for bokstav in kryptert_melding:
        if bokstav.isalpha():
            # Beregner den dekrypterte bokstaven ved å forskyve i alfabetet i motsatt retning
            dekryptert_bokstav = chr((ord(bokstav.lower()) - ord('a') - forskyvning) % 26 + ord('a'))
            # Bevarer original bokstavens case
            if bokstav.isupper():
                dekryptert_bokstav = dekryptert_bokstav.upper()
            dekryptert_melding += dekryptert_bokstav
        else:
            # Beholder ikke-bokstaver uendret
            dekryptert_melding += bokstav

    return dekryptert_melding

# Hovedprogram
kryptert_melding = input("Skriv inn den krypterte meldingen: ")
forskyvning = int(input("Skriv inn antall forskyvninger: "))

dekryptert_resultat = dekrypter_melding(kryptert_melding, forskyvning)

print(f"Den dekrypterte meldingen er: {dekryptert_resultat}")
