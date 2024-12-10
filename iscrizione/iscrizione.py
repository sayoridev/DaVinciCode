def calcola_quota(reddito, media_voti):
    quota = 0
    if media_voti < 7:
        quota = 35.00
    elif 7 <= media_voti <= 8:
        quota = 22.00
    else:
        quota = 18.00
    
    if reddito < 16000:
        quota *= 0.7
    elif reddito > 16000:
        quota *= 1.2
    
    return round(quota, 2)

# Esempio di utilizzo:
reddito = input("Inserisci il tuo reddito: ")
media_voti = input("Inserisci la media dei voti: ")
print(calcola_quota(reddito, media_voti))

