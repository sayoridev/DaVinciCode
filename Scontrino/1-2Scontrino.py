#library
from datetime import datetime

#variable
numart = 0
costounit = 10.5
costotot = 0.0
costonetto = 0.0

#time
myobj = datetime.now()

#main
numart = float(input("Inserisci il numero di articoli: "))

costonetto = numart * costounit
costotot = ((costonetto * 22)/100) + costonetto #iva 22$


if(numart < 3):
    costoscontato = costotot
    print("Non hai a disposizione nessuno sconto")
elif(numart >= 3 and numart < 5):
    print("Hai a disposizione il 10% di sconto")
    costoscontato = costotot - ((costotot*10)/100)
    costoscontato = round(costoscontato,2)
    sconto = "del 10%"
elif(numart >=5 and numart <10):
    print("Hai a disposizione il 15% di sconto")
    costoscontato = costotot - ((costotot*15)/100)
    costoscontato = round(costoscontato,2)
    sconto = "del 15%"
else:
    print("Hai a disposizione il 25% di sconto")
    costoscontato = costotot - ((costotot*25)/100)
    costoscontato = round(costoscontato,2)
    sconto = "del 25%"


print("\n****************************************\n")
print("Orario stampa scontrino: ", myobj)
print("\nNumero Articoli: ", numart)
print("Costo Unitario: ", costounit)
print("Costo Netto: ", costonetto)
print("Costo totale: ", costotot)
print("Sconto: ", sconto)
print("Costo scontato: ", costoscontato)
print("\n****** CON IVA AL 22% ******\n")
