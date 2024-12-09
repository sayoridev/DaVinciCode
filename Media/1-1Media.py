#variabili
voto1 = 0
voto2 = 0
voto3 = 0

#inserire voti verifica
voto1 = float(input("Inserisci il voto della prima verifica: "))
voto2 = float(input("\nInserisci il voto della seconda verifica: "))
voto3 = float(input("\nInserisci il voto della terza verifica: "))
print("\n******************************************************")

#calcolo media
mediatot = voto1 + voto2 + voto3/3

#if media
if mediatot < 3:
    print("Giudizio Nullo")
else:
    print("letgoski")