'''
Egy hotel reggelizési lehetőséget is biztosít a vendégei számára. A mai napon tojásrántotta lesz a reggeli.
A hotel séfje úgy számol, hogy vendégenként 3 db tojásra lesz szükség a rántottához, 
de a hibás vagy törött darabok miatt mindig 10%-kal többet vesznek, mint amennyi szükséges lenne.
Készíts reggeli.py néven programot, amely segíti a bevásárlás megtervezését.
A program először kérje be a vendégek számát, és hogy hány darab tojás van a raktárban.
Ezt követően számolja ki és írja ki a képernyőre, hogy mennyi tojás szükséges ennyi vendég rántottájához!
Ne feledkezz meg a hulladékról és arról sem, hogy csak egész számú tojás létezik!
Ezt követően állapítsa meg a program, hogy szükséges-e még tojást vásárolni, és ha igen, akkor hány darabot!
Ezeket az információkat is írja ki a képernyőre a minta szerint!
'''


#minta:
# Vendégek száma: 12
# Raktáron lévő tojások: 30
# Ennyi vendéghez 40 tojásra van szükség.
# Kell még 10 tojást vásárolni.
# Vendégek száma: 20
# Raktáron lévő tojások: 70
# Ennyi vendéghez 66 tojásra van szükség.
# Nem kell több tojást vásárolni.
import math


vendegek_szama = int(input("Vendégek száma: "))
tojasok_szama = int(input("Raktáron lévő tojások: "))
kell_tojas = int(vendegek_szama * 3) * 1.1
kerekitve_tojas = math.ceil(kell_tojas)
print(f"Ennyi vendéghez {kerekitve_tojas} tojásra van szükség.")
meg_tojas = kerekitve_tojas - tojasok_szama
if kerekitve_tojas <= tojasok_szama:
    print("Nem kell több tojást vásárolni.")
else:
    print(f"Kell még {meg_tojas} tojást vásárolni.")