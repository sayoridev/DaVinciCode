# Variabili
voto1 = 0
voto2 = 0
voto3 = 0

# Inserire voti verifica
voto1 = float(input("Inserisci il voto della prima verifica: "))
voto2 = float(input("\nInserisci il voto della seconda verifica: "))
voto3 = float(input("\nInserisci il voto della terza verifica: "))
print("\n******************************************************")

# Calcolo media
mediatot = (voto1 + voto2 + voto3) / 3

# If media
if mediatot < 3:
    print("Giudizio Nullo")
    print("\nImpegnati se non vuoi essere bocciatio!")
elif mediatot < 4.5:
    print("Gravemente insufficiente")
    print("\nMale Male vedi di impegnarti di più!")
elif mediatot < 6:
    print("Insufficiente")
    print("\nCi sei quasi ancora impegnati ancora un pochino!")
elif mediatot < 7.5:
    print("Sufficiente")
    print("\nSe vuoi puoi puntare più in alto")
elif mediatot < 9:
    print("Buono")
    print("\nBuono continua così!")
else:
    print("Eccellente")
    print("\nStraordinario!")