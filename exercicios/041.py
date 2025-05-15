import datetime
import sys
nasci = int(input("Ano de nascimento: "))
anoatual = datetime.datetime.now()
anoatual = anoatual.year
idade = anoatual - nasci
if 0>idade:
    print("Insira um ano valido")
    sys.exit()    
print(f"O atleta tem {idade}")

if 0 < idade <= 9:
    print("Classificação: MIRIM")
elif 9 < idade <= 14:
    print("Classificação: INFANTIL")
elif 14 < idade <= 19:
    print("Classificação: JUNIOR")
elif 19 < idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
