from os import system
from time import sleep
from os import path

def chargement(message = 'Chargement en cours ...',tour = 2,sprite=['| ','/ ','- ',"\ "]):#-------------------------------------------------------------Juste pour le kiff :) !...
    for i in range(0,tour):
        for j in sprite:
            print(message,j)
            sleep(0.20)
            system('cls')
    print(f" {message.split(' ')[0]} terminé avec succes :) !...")
    sleep(1.10)
    system('cls')

