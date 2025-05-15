import datetime
nasci = int(input("Ano nascimento: "))
anoatual = datetime.datetime.now()
anoatual = anoatual.year
idade = anoatual - nasci
alist = idade - 18
print(f"Quem nasceu em {nasci} tem {idade} anos em 2025")

if idade < 18:
    print(f"Ainda faltam {alist * (-1)} anos para voce se alistar")
elif idade > 18:
    print(f"Voce ja deveria ter se alistado há {alist} anos")
elif idade == 18:
    print("Voce tem que se alistar IMEDIATAMENTE")
    
