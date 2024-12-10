def applica_sconto(prezzo):
    if prezzo < 30.00:
        prezzo -= prezzo * 0.12
    else:
        prezzo -= prezzo * 0.25
    return round(prezzo, 2)

# Esempio di utilizzo:
prezzo_iniziale = input("Inserisci il prezzo iniziale: ")
print(applica_sconto(prezzo_iniziale))

