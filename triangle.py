n = int(input("Inserisci l'altezza del triangolo isoscele: "))

print("Ecco il triangolo isoscele:")
for i in range(n + 1):
    for j in range(i+1):
        print("*",end='')
    print("")

