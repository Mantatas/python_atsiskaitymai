# 1. Suvedam sveiką teigiamą skaičių n (tarkim 100). Programa sugeneruoja atsitiktinį skaičių nuo 1 iki n 
# Sugeneravus atsitiktinį skaičių vartotojui siūloma atspėti kokį skaičių sugeneravo programa. 
# Įvedus spėjamą skaičių (tarkim 75) programa praneša ar sugeneruotas skaičius didesnis ar mažesnis už 
# įvestą skaičių ir siūlo spėti dar kartą (tarkim „Sugeneruotas skaičius didesnis už 75. Atliksite 3 spėjimą...“). 
# Įvedus bet kokius simbolius ar neigiamus skaičius programa prašo kartoti įvedimą ir jo neprisumuoja prie spėjimų 
# skaičiaus. Vartotojui atspėjus skaičių rodomas pranešimas, koks buvo sugeneruotas skaičius ir kiek spėjimų buvo atlikta. 
# Pabaigus žaidimą –siūloma sužaisti dar kartą. Žaidimo programavime panaudoti funkcijas. Be žaidimo paslaugos programa 
# sukuria žaidimo „registravimo“ failą reg.txt, kuriame yra pateikiama informacija apie žaidimo eigą. 

import random

with open("file01.txt", "w") as file:
    pass

def spejimas():
    while True:
        try:
            n = int(input('ivesk sveika teig. sk. '))
            if n <= 0:
                print('ivestas sk. turi buti teigiamas.')
                continue
            break
        except ValueError:
            print('netinkamas simbolis/skaicius. turi buti sveikas teigiamas skaicius.')

        
    randNr = random.randint(1, n)
    with open("file01.txt", "a") as file:
        file.write(f'sugeneruotas skaicius {randNr}\n')

    spejimuSk = 0
    netinkNr = 0

    while True:
        try:
            spejimuSk += 1
            userSpejimas = int(input('koks spejimas? '))
            if userSpejimas < 1 or userSpejimas > n:
                netinkNr += 1
                spejimuSk -= 1
                print('netinkamas numeris. bandyk darkart.')
                with open("file01.txt", "a") as file:
                    file.write(f'pasirinktas netinkamas numeris. useris trolina {netinkNr} kartu.\n')
                continue
            if userSpejimas == randNr:
                with open("file01.txt", "a") as file:
                    file.write(f'skaicius atspetas is {spejimuSk} kartu(s).\n\n')
                print(f'sveikinimai! atspejote! bandymu: {spejimuSk}, netinkamu skaiciu bandymu: {netinkNr}')
                break
            if userSpejimas != randNr:
                if userSpejimas > randNr:
                    with open("file01.txt", "a") as file:
                        file.write(f'neatspeta su {userSpejimas}. skaicius buvo mazesnis. spejimo nr: {spejimuSk}\n')
                    print(f'neatspejote. sugeneruotas sk. mazesnis uz {userSpejimas}. cia buvo jusu {spejimuSk} spejimas.')
                else:
                    with open("file01.txt", "a") as file:
                        file.write(f'neatspeta su {userSpejimas}. skaicius buvo didesnis. spejimo nr: {spejimuSk}\n')
                    print(f'neatspejote. sugeneruotas sk. didesnis uz {userSpejimas}. cia buvo jusu {spejimuSk} spejimas.')
        except ValueError:
            print(f'netinkamas simbolis/skaicius. turi buti sveikas teigiamas skaicius, kuris tarp 1 ir {n}.')
            spejimuSk -= 1

spejimas()

zaistaKartu = 1

ats = input('ar norite zaisti darkart? (taip/ne) ')
while ats == 'taip':
    zaistaKartu += 1
    spejimas()
    ats = input('ar norite zaisti darkart? (taip/ne) ')
    if ats != 'taip':
        with open("file01.txt", "a") as file:
            file.write(f'buvo zaista {zaistaKartu} kartu(s)')