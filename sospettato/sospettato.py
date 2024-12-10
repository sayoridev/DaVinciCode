def identifica_sospetto(altezza_adamo, altezza_eva):
    distanza_impronte = 0.65
    altezza_calcolata = 3 * distanza_impronte
    if abs(altezza_adamo - altezza_calcolata) < abs(altezza_eva - altezza_calcolata):
        return "Adamo"
    else:
        return "Eva"

# Esempio di utilizzo:
altezza_adamo = 1.95
altezza_eva = 1.80
print(identifica_sospetto(altezza_adamo, altezza_eva))

