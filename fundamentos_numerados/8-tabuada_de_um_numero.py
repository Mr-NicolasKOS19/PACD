# Programa simples: Tabuada
import os

resposta = "sim"
while resposta in ["sim", "s"]:
    os.system('cls')
    
    try:
        n = int(input("Valor a ser calculado: "))
        
        print(f"\n{'Tabuada de ' + str(n):^30}\n")
        for i in range(1, 11):
            resultado = n * i
            print(f"{n:3d} × {i:2d} = {resultado:4d}")
        
        # Loop para validar resposta
        resposta_valida = False
        while not resposta_valida:
            resposta = input("\n\nDeseja ver mais tabuadas (sim/não)? ").lower()
            
            if resposta in ["sim", "s"]:
                resposta_valida = True
                resposta = "sim"
            elif resposta in ["não", "n"]:
                print("\nAté logo!")
                resposta_valida = True
                resposta = "não"
            else:
                print("❌ Resposta inválida! Digite apenas 'sim' ou 'não'.")
        
        # Finalizar se responder "não"
        if resposta == "não":
            break
            
    except ValueError:
        print("❌ Erro: Digite um número inteiro válido!")
        input("Pressione ENTER para tentar novamente...")
