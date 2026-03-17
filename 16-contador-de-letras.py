import os
os. system ("cls")
frase = str(input("Digite uma frase por favor: "))

letras_apenas = len(frase.replace(" ", ""))
print(f"Total de letras (sem espaços): {letras_apenas}")