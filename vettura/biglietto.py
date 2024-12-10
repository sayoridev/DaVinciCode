def calcola_biglietto(tipo_veicolo, cilindrata):
    if tipo_veicolo.lower() == "autovettura":
        if cilindrata <= 1000:
            return 20
        elif cilindrata <= 2000:
            return 30
        else:
            return 40
    elif tipo_veicolo.lower() == "camion":
        if cilindrata <= 2000:
            return 40
        elif cilindrata <= 3000:
            return 50
        else:
            return 100
    else:
        return "Tipo di veicolo non valido"

tipo_veicolo = input("Inserisci il tipo di veicolo: ")
cilindrata = input("Inserisci la cilindrata del veicolo: ")
print(calcola_biglietto(tipo_veicolo, cilindrata))

