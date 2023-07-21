import os
import time
import random

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


nombre_aleatoire = ""
score = 0

for i in range(4):
    nombre_aleatoire += str(random.randint(0, 9))

while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(nombre_aleatoire)
    time.sleep(3)
    clear_screen()
    demander_nombre = input("Votre réponse: ")
    if demander_nombre != nombre_aleatoire:
        break
    else:
        nombre_aleatoire += str(random.randint(0, 9))
        score += 1
    clear_screen()
    print("Bonne réponse")
    print(f"Score: {score}")
    time.sleep(2)
    clear_screen()

clear_screen()
print(f"Mauvaise réponse, la réponse était {nombre_aleatoire}")
print(f"Votre score est de {score}")