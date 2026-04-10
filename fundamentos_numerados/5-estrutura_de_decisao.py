import os
"""
classifique fase da vida

este codigo le uma idade e informa a fase da vida

"bebe", quando a idade for menor ou igual a 2
"criança", quando a idade for menor ou igual a 10
"pre-adolescente", menor que 15
"adolescente", menor  que 18
"jovem", menor ou igual a 30
"adulto", menor que 60
"melhor idade", maior ou igual a 60

"""
idade = int(input("digite a idade: "))

if idade <= 2:
    print("bebe")
elif idade <= 10:
    print("criança")
elif idade < 15:
    print("pré-adolescente")
elif idade < 18:
    print("adolescente")
elif idade <= 30:
    print("jovem")
elif idade < 60:
    print("adulto")
else:
    print("melhor idade")
