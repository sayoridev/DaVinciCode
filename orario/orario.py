def controlla_orario(h, m, s):
    if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
        return "Orario corretto"
    else:
        return "Orario errato"

# Esempio di utilizzo:
h, m, s = 15, 30, 45
print(controlla_orario(h, m, s))