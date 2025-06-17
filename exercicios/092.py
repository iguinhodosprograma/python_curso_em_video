pessoa = {}
idade_contratacao = 0

pessoa["nome"] = input("Nome: ").capitalize()
pessoa["idade"] = int(input("Ano de Nascimento: "))
nascimento = pessoa["idade"]
pessoa["clt"] = int(input("Carteira de Trabalho (caso não tenha digite 0): "))
pessoa["idade"] = 2025 - pessoa["idade"]

if pessoa["clt"] != 0:
    pessoa["contratacao"] = int(input("Ano de Contratação: "))
    idade_contratacao = pessoa["contratacao"] - nascimento
    pessoa["salario"] = float(input("Salário: R$"))
    pessoa["aposentadoria"] = ((pessoa["contratacao"] - nascimento) + 35) - (pessoa["contratacao"] - nascimento) + idade_contratacao

    
for k, v in pessoa.items():
    print(f" - {k} tem o valor {v}")
