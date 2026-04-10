import os
os.system("cls")

a = int(input("Digite o termo inicial: "))
b = int(input("Digite o termo final: "))
c = int(input("Informe a cardinalidade: "))

numeros = list(range(a, b+1, c))
if numeros:
    print(", ".join(map(str, numeros)))
else:
    print("Nenhum número para exibir com esses parâmetros")
