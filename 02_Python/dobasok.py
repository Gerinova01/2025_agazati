import random as r

ertek2 = 4
ertek3 = 8

def közte(ertek1, ertek2, ertek3):
    if ertek1>ertek2 and ertek1<ertek3:
        return True
    else:
        return False
    
dobas = 0
for i in range(150):
    sok_szam = r.randint(1,12)
    if közte(sok_szam, ertek2, ertek3):
        dobas += 1

szazalek = (dobas / 150) * 100

print(f"A 150 dobásból {dobas} esett 4 és 8 közé.")
print(f"Ez az összes dobás {szazalek:.2f}%-a.")