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


def zaidimas(lazdeliuSk):
    player1 = input('Koks pirmo zaidejo vardas? ')
    if player1 == '':
        player1 = 'Player1'
    player2 = input('Koks antro zaidejo vardas? ')
    if player2 == '':
        player2 = 'Player2' 

    players = [player1, player2]
    pirmas = random.choice(players)

    guessSum = 0
    guessAmt = 0

    if pirmas == player1:
        print(f'Pirmas pradeda {player1}. lazdeliu is viso {lazdeliuSk}')
        while lazdeliuSk >= 0:
            guess1 = int(input(f'koks {player1} spejimas?'))
            if guess1 < 1 or guess1 > 3:
                print(f'Neteisingas {player1} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            guessSum += guess1
            guessAmt += 1
            lazdeliuSk -= guess1
            print(f'{player1} {guessAmt} pasirinkimu paeme {guess1}. lazdeliu liko {lazdeliuSk}')
            if lazdeliuSk == 0:
                print(f'pralaimejote. laimejo {player2}')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue
            
            guess2 = int(input(f'Koks {player2} spejimas? '))
            if guess2 < 1 or guess2 > 3:
                print(f'Neteisingas {player2} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            guessSum += guess2
            lazdeliuSk -= guess2
            print(f'{player2} {guessAmt} pasirinkimu paeme {guess2}. lazdeliu liko {lazdeliuSk}')
            if lazdeliuSk == 0:
                print(f'pralaimejote. laimejo {player1}')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue
    else:
        print(f'Pirmas pradeda {player2}. lazdeliu is viso {lazdeliuSk}')
        while lazdeliuSk > 0:
            guess2 = int(input(f'koks {player2} spejimas?'))
            if guess2 < 1 or guess2 > 3:
                print(f'Neteisingas {player2} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            guessSum += guess2
            guessAmt += 1
            lazdeliuSk -= guess2
            print(f'{player2} {guessAmt} pasirinkimu paeme {guess2}. lazdeliu liko {lazdeliuSk}')
            if lazdeliuSk == 0:
                print(f'pralaimejote. laimejo {player1}')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue
            
            guess1 = int(input(f'Koks {player1} spejimas? '))
            if guess1 < 1 or guess1 > 3:
                print(f'Neteisingas {player1} pasirinkimas. Turi buti nuo 1 iki 3.')
                continue
            guessSum += guess1
            lazdeliuSk -= guess1
            print(f'{player1} {guessAmt} pasirinkimu paeme {guess1}. lazdeliu liko {lazdeliuSk}')
            if lazdeliuSk == 0:
                print(f'pralaimejote. laimejo {player2}')
                break
            elif lazdeliuSk < 0:
                print('Skaicius per didelis. Pasirinkite mazesni.')
                continue

    


lazdeliuSk = int(input('Kiek lazdeliu is viso? '))
zaidimas(lazdeliuSk)

zaistaKartu = 1

ats = input('ar norite zaisti darkart? (taip/ne) ')
while ats == 'taip':
    zaistaKartu += 1
    lazdeliuSk = int(input('Kiek lazdeliu is viso? '))
    zaidimas(lazdeliuSk)
    ats = input('ar norite zaisti darkart? (taip/ne) ')