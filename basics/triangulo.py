
#testando sequencia logica e atribuiçoes de variaveis

""" 
este codigo le dois numero do tipo float 
representando base e altura e calcula a area do triangulo
"""
import os
resposta = "sim"
while resposta == "sim":
    # entradas
    os.system('cls')

    base = float(input("informe o valor da base: "))
    altura = float(input("informe o valor da altura: "))

    area = (base * altura) / 2

    print(f"a area do triangulo é {area}")
    resposta = input("\ndeseja continuar (sim/não)? ")