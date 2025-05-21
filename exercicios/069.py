homens = 0
maioridade = 0
vintemulher = 0
while True:
    print("-"*20)
    print("CADASTRE UMA PESSOA")
    print("-"*20)
    idade = int(input("Idade: "))
    if idade > 18:
        maioridade += 1 
    sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        vintemulher += 1
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {maioridade}")
print(f"Total de homens cadastrados: {homens}")
print(f"Total de mulheres com menos de 20 anos: {vintemulher}")