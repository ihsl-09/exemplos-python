import os
os.system ("cls")
import random
numero = random.randint(1, 100)
guess = int(input("Chute um Numero de um a cem: "))

if guess == numero:
    print("Acertou!!!!")
elif guess >= numero:
    print("Maior que o Numero")
elif guess <= numero:
    print("Menor que o Numero")
    




