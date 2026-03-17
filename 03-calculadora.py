import os
os.system ("cls")
valor01 = int(input("Digite o Pimeiro Valor: "))
valor02 = int(input("Digite o Segundo Valor: "))
calculo = int(input("Digite qual Calculo Deseja, Digite + Para Soma, - Para Sub, * Para Mult, / Para Div: "))
soma = valor01 + valor02
sub = valor01 - valor02
mult = valor01 * valor02
div = valor01 / valor02
if (calculo == "+"):
    print("A Soma desses Valores é: ",soma)
elif (calculo == "-"):
    ("A Subtração desses Valores é: ",sub)
elif (calculo == "*"):
    print("A Multiplicação desses Valores é: ",mult)
elif (calculo == "/"):
    print("A Divisão desses Valores é: ",div)
else:
    print("Opção Invalida")