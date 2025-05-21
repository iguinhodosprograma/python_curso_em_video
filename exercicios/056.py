media = 0
somaidade = 0
maioridadehomem = 0
nomemaisvelho = ""
idademulher = 0
mulher = 0
for c in range(1,5):
    print("{:=^40}ª pessoa". format(c))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ")
    somaidade += idade
    if sexo in "Ff" and idade < 20:
        idademulher = idade
        mulher += 1
    if c == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
media = somaidade / 4
print(f"A media de idade do grupo é de {media} anos")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomemaisvelho}")    
print(f"No grupo existem {mulher} mulheres com menos de 20 anos")

