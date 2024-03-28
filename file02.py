# Suprogramuokite seną kinų žaidimą lazdomis. Žaidžia du žaidėjai. Yra 10 lazdelių. Žaidėjai paeiliui ima nuo vienos
# iki trijų lazdų. Pirmas žaidimą pradeda kompiuterio atsitiktiniu būdu sugeneruotas žaidėjas (tai gali būti žaidėjas Nr.1
# arba žaidėjas Nr.2, jei yra suvedami žaidėjų vardai kompiuteris atsitiktiniu būdu parenka žaidėjo vardą). Žaidimas
# tęsiasi tol, kol nesibaigia lazdelės. Pralaimi tas, kuris paėmė paskutinę lazdelę.
# Suprogramuokite žaidimą taip, kad galėtų žaisti du žmonės. Žaidimo pradžioje yra 10 lazdelių. Kiekviename žaidimo
# etape atspausdinamas žaidėjo numeris, lazdelių skaičius, ir užklausa, kiek lazdelių paims žaidėjas. Nepamirškite
# pakeisti žaidėjų eilės numerius ir mažinti lazdelių skaičių. Nepamirškite, pabaigoje išvesti laimėjusio žaidėjo numerio.
# Nepamirškite, kad žaidėjas negali paimti daugiau nei tris lazdeles (apsaugokite ir nuo 0 ir neigiamų skaičių), ir taip pat
# negali paimti lazdelių daugiau nei liko. Žaidimo detalės gali skirtis. Galime suvesti žaidėjų vardus. Galima keisti pradinį lazdelių skaičių.
# Be žaidimo paslaugos programa sukuria žaidimo „registravimo“ failą reg.txt, kuriame yra pateikiama informacija apie žaidimo eigą.

import random

with open("file02.txt", "w") as file:
    pass

def zaidimas(lazdeliuSk):

    player1 = input('Koks pirmo zaidejo vardas? ')
    if player1 == '':
        player1 = 'Player1'
    player2 = input('Koks antro zaidejo vardas? ')
    if player2 == '':
        player2 = 'Player2' 

    players = [player1, player2]
    pirmas = random.choice(players)

    with open("file02.txt", "a") as file:
        file.write(f'Zaideju vardai: {player1} ir {player2}\nLazdeliu skaicius: {lazdeliuSk}\nZaidima pradeda {pirmas}\n')
                   
    guessAmt = 0

    if pirmas == player1:
        print(f'Pirmas pradeda {player1}. lazdeliu is viso {lazdeliuSk}')
        while lazdeliuSk >= 0:
            guess1 = int(input(f'koks {player1} spejimas? '))
            if guess1 < 1 or guess1 > 3:
                print(f'Neteisingas {player1} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            guessAmt += 1
            lazdeliuSk -= guess1

            if lazdeliuSk == 0:
                print(f'laimejo {player2}')
                with open("file02.txt", "a") as file:
                    file.write(f'laimejo {player2}\n\n')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue

            print(f'{player1} {guessAmt} pasirinkimu paeme {guess1}. lazdeliu liko {lazdeliuSk}')
            with open("file02.txt", "a") as file:
                file.write(f'{player1} paima {guess1} lazdeles. Liko {lazdeliuSk}\n')

            
            guess2 = int(input(f'Koks {player2} spejimas? '))
            if guess2 < 1 or guess2 > 3:
                print(f'Neteisingas {player2} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            lazdeliuSk -= guess2
            
            if lazdeliuSk == 0:
                print(f'pralaimejote. laimejo {player1}')
                with open("file02.txt", "a") as file:
                    file.write(f'laimejo {player1}\n\n')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue

            print(f'{player2} {guessAmt} pasirinkimu paeme {guess2}. lazdeliu liko {lazdeliuSk}')
            with open("file02.txt", "a") as file:
                file.write(f'{player2} paima {guess2} lazdeles. Liko {lazdeliuSk}\n')

    else:
        print(f'Pirmas pradeda {player2}. lazdeliu is viso {lazdeliuSk}')
        while lazdeliuSk > 0:
            guess2 = int(input(f'koks {player2} spejimas? '))
            if guess2 < 1 or guess2 > 3:
                print(f'Neteisingas {player2} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            guessAmt += 1
            lazdeliuSk -= guess2

            if lazdeliuSk == 0:
                print(f'pralaimejote. laimejo {player1}')
                with open("file02.txt", "a") as file:
                    file.write(f'laimejo {player1}\n\n')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue

            print(f'{player2} {guessAmt} pasirinkimu paeme {guess2}. lazdeliu liko {lazdeliuSk}')
            with open("file02.txt", "a") as file:
                file.write(f'{player2} paima {guess2} lazdeles. Liko {lazdeliuSk}\n')
            
            guess1 = int(input(f'Koks {player1} spejimas? '))
            if guess1 < 1 or guess1 > 3:
                print(f'Neteisingas {player1} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            lazdeliuSk -= guess1

            if lazdeliuSk == 0:
                print(f'laimejo {player2}')
                with open("file02.txt", "a") as file:
                    file.write(f'laimejo {player2}\n\n')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue

            print(f'{player1} {guessAmt} pasirinkimu paeme {guess1}. lazdeliu liko {lazdeliuSk}')
            with open("file02.txt", "a") as file:
                file.write(f'{player1} paima {guess1} lazdeles. Liko {lazdeliuSk}\n')

    


lazdeliuSk = int(input('Kiek lazdeliu is viso? '))
zaidimas(lazdeliuSk)

zaistaKartu = 1

ats = input('ar norite zaisti darkart? (taip/ne) ')
while ats == 'taip':
    with open("file02.txt", "a") as file:
        file.write(f'Pasirinko zaisti\n\n')
    zaistaKartu += 1
    lazdeliuSk = int(input('Kiek lazdeliu is viso? '))
    zaidimas(lazdeliuSk)
    ats = input('ar norite zaisti darkart? (taip/ne) ')
else:
    with open("file02.txt", "a") as file:
        file.write(f'Pasirinko nebezaisti. zaista {zaistaKartu} kartu(s).\n')