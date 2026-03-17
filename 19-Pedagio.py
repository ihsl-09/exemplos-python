import os
os.system ("cls")
veiculo = int(input("Ola, em qual veiculo você se encontra no momento, 1-Carro 2-Moto 3-Caminhão"))

if veiculo == 1:
    print("O valor do pedagio é 10 reais")
elif veiculo == 2:
    print("O valor do pedagio é 5 reais")
elif veiculo == 3:
    print("O valor do pedagio é 20 reais")
else:
    print("VALOR COLOCADO INEXISTENTE")