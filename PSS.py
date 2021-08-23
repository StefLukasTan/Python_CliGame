import os
import random
import pyfiglet
os.system('clear')

choice = ["Gunting", "Batu", "Kertas"]

win = 0
lose = 0
draw = 0

print (pyfiglet.figlet_format("GunBatKer!"))
print ("Created by StefLukasTan")

while True:
    print ("""
0. Gunting
1. Batu
2. Kertas""")
    inp = int(input('Masukkan pilihan Anda: '))

    player = choice[inp]
    comp = choice[random.randint(0, 2)]

    while player == 'Gunting':
        if comp == "Gunting":
            print ("Hasil: Seri")
            draw += 1
            break
        elif comp == "Batu":
            print ("Hasil: Anda kalah!")
            lose += 1
            break
        else:
            print ("Hasil: Anda menang!")
            win += 1
            break

    while player == "Batu":
        if comp == "Gunting":
            print ("Hasil: Anda menang!")
            win += 1
            break

        elif comp == "Batu":
            print ("Hasil: Seri")
            draw += 1
            break
        else:
            print ("Hasil: Anda kalah!")
            lose += 1
            break

    while player == "Kertas":
        if comp == "Gunting":
            print ("Hasil: Anda kalah!")
            lose += 1
            break
        elif comp == "Batu":
            print ("Hasil: Anda menang!")
            win += 1
            break
        else:
            print ("Hasil: Seri!")
            draw += 1
            break

    print ("\nWin: ", win)
    print ("Lose: ", lose)
    print ("Draw: ", draw)


