numeros = []  # cria uma lista de números

p = 0
i = 1
while p != "-999":
    p = input(f"informe o {i}º número: ")
    if p != "-999":
        numeros.append(int(p))
    i += 1

# Cálculos Cabulosos
quantidade = len(numeros)
pares = sum(1 for n in numeros if n % 2 == 0)
impares = sum(1 for n in numeros if n % 2 != 0)
somatoria = sum(numeros)
media = somatoria / quantidade if quantidade > 0 else 0
maior = max(numeros) if quantidade > 0 else None
posicao_maior = numeros.index(maior) if quantidade > 0 else None
menor = min(numeros) if quantidade > 0 else None

# Saídas Extremamente Interessantes
print("\n" + "="*50)
print(f"foram informados {quantidade} números")

if quantidade > 0:
    print(f"foram informados {pares} números pares")
    print(f"foram informados {impares} números impares")
    print(f"a somatória dos números é {somatoria}")
    print(f"o maior número foi {maior} na posição {posicao_maior}")
    print(f"o menor número foi {menor}")
    print(f"a média aritmética foi {media:.2f}")
else:
    print("Nenhum número foi informado")

print("="*50)