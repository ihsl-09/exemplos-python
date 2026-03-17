import os
os. system ("cls")

print("Seja Bem vindo ao checa estoque do orfanato santa mega freira.")
quant = int(input("Por favor insira a quantidade de produtos em estoque: "))

if quant < 5:
    print("Estoque baixo, por favor preencha")
if quant >= 5:
    print("Estoque Okay") 