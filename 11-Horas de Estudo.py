import os
os. system("cls")
nome = str(input("Insira Seu nome por favor:"))
print("Ola",nome)
horas = int(input("Quantas Horas por dia você estuda? "))

if horas < 2:
    print("Poucas Horas De estudo seria melhor aumentar.")
elif horas == 4:
    print("Horas medianas, mas pode haver possivel aumento.")
elif horas > 4:
    print("Você está de parabens")