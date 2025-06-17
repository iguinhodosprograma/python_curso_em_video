simnao = "s"
pessoas = []
p = 0
pessoa = {}
cont = 0
soma = 0
mulheres = []
while simnao in "Ss":
    pessoa["nome"] = input("Nome: ").capitalize()
    pessoa["sexo"] = input("Sexo: [M/F] ").upper()
    while pessoa["sexo"] not in "MmFf":
        pessoa["sexo"] = input("ERRO! Digite apenas M ou F: ").upper()
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]
    
    if pessoa["sexo"] == "F":
        mulheres.append(pessoa["nome"])
        
    pessoas.append(pessoa.copy())
    del(pessoa["nome"], pessoa["idade"], pessoa["sexo"])
    cont += 1
    
    simnao = input("Quer continuar? [S/N] ").upper()
    while simnao not in "SsNn":
        simnao = input("ERRO! Digite apenas S ou N ").upper()
    if simnao in "Nn":
        break
    
media = soma/cont

print(f"A) Ao todo temos {cont} pessoa cadastradas.")
print(f"B) A media de idade é de {media:.2f} anos")
print(f"C) As mulheres cadastradas foram", end = ", ")
print(*mulheres)
print("D) lista das pessoas que estão acima da média")

for pessoa in pessoas:
    if pessoa["idade"] > media:
        print(f"    nome = {pessoa['nome']}, sexo = {pessoa['sexo']}, idade = {pessoa['idade']}")

print("<< ENCERRADO >>")
    
    
    