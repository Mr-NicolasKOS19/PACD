import os
#Calcular a área de um triângulo
"""
Este código calcula a área do triângulo
a partir da base e altura
"""
os.system('cls') #limpe os dados da tela
base = float(input("informe o valor da base: "))
altura = float(input("informe o valor da altura: "))
#Calculando a área 
area = base * altura / 2

#Mostrando o resultado 
print(f"A área do triângulo é {area}.")