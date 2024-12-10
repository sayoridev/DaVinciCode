n = int(input("Inserisci il numero di colonne che vuoi: "))

print("Verranno stampate " + str(n) + " colonne")

for i in range(n):
    for j in range(n):  
        print("*", end="")  
    print()

