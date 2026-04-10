#Ler n palavras guardando-as em uma lista

palavra=[] # cria uma lista palavra[]

p = ""
i = 1
while p!="fim" :
    p = input(f"informe a {i}ª palavra: ")
    if p!= "fim":
        palavra.append(p)
    i+=1
    # Aqui esta fora do if
# Aqui esta fora do while 
print("palavra")
for i, p in enumerate(palavra,start=1):
    print(f"{i}ª = {p}")

print(palavra.sort())
