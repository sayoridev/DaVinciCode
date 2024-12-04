#variabili
numart = 0
costounit = 10.5
costotot = 0.0
costonetto = 0.0

#main
numart = float(input("Inserisci il numero di articoli: "))

costonetto = numart * costounit
costotot = ((costonetto * 22)/100) + costonetto #iva 22$

print("\n****************************************\n")
print("Numero Articoli: ", numart)
print("Costo Unitario: ", costounit)
print("Costo Netto: ", costonetto)
print("Costo totale: ", costotot)
print("\n****** CON IVA AL 22% ******\n")
